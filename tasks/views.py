"""
Views for the tasks application.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    View
)
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.utils import timezone
from .models import Task, UserProfile
from .forms import TaskForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class HomeView(TemplateView):
    """Home page view."""
    template_name = 'tasks/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['total_tasks'] = Task.objects.filter(user=self.request.user).count()
            context['completed_tasks'] = Task.objects.filter(
                user=self.request.user,
                status='completed'
            ).count()
            context['pending_tasks'] = Task.objects.filter(
                user=self.request.user,
                status='pending'
            ).count()
        return context


class AboutView(TemplateView):
    """About page view."""
    template_name = 'tasks/about.html'


class RegisterView(View):
    """User registration view."""
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('task-list')
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            messages.success(request, f'Account created successfully for {user.username}! You can now log in.')
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    """User profile view."""
    
    def get(self, request):
        # Get or create user profile
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=user_profile)
        
        # Get user statistics
        total_tasks = Task.objects.filter(user=request.user).count()
        completed_tasks = Task.objects.filter(user=request.user, status='completed').count()
        pending_tasks = Task.objects.filter(user=request.user, status='pending').count()
        high_priority = Task.objects.filter(user=request.user, priority='high').count()
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'high_priority': high_priority,
        }
        return render(request, 'registration/profile.html', context)
    
    def post(self, request):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'registration/profile.html', context)


class TaskListView(LoginRequiredMixin, ListView):
    """List view for tasks."""
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        
        # Filter by status
        status_filter = self.request.GET.get('status')
        if status_filter:
            if status_filter == 'active':
                queryset = queryset.exclude(status='completed')
            elif status_filter == 'completed':
                queryset = queryset.filter(status='completed')
        
        # Filter by priority
        priority_filter = self.request.GET.get('priority')
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)
        
        # Search
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        # Sort
        sort_by = self.request.GET.get('sort', '-created_at')
        queryset = queryset.order_by(sort_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', 'all')
        context['priority_filter'] = self.request.GET.get('priority', '')
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_by'] = self.request.GET.get('sort', '-created_at')
        
        # Statistics
        all_tasks = Task.objects.filter(user=self.request.user)
        context['total_count'] = all_tasks.count()
        context['active_count'] = all_tasks.exclude(status='completed').count()
        context['completed_count'] = all_tasks.filter(status='completed').count()
        context['overdue_count'] = sum(1 for task in all_tasks if task.is_overdue)
        
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a single task."""
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create view for tasks."""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create New Task'
        context['button_text'] = 'Create Task'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Update view for tasks."""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Task'
        context['button_text'] = 'Update Task'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Delete view for tasks."""
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)


class TaskToggleView(LoginRequiredMixin, View):
    """Toggle task completion status."""
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        
        if task.status == 'completed':
            task.mark_pending()
            messages.info(request, f'Task "{task.title}" marked as pending.')
        else:
            task.mark_completed()
            messages.success(request, f'Task "{task.title}" marked as completed!')
        
        return redirect('task-list')
