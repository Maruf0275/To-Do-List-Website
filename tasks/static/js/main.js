// =====================
// Mobile Menu Toggle
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger
            const spans = hamburger.querySelectorAll('span');
            spans.forEach((span, index) => {
                if (navMenu.classList.contains('active')) {
                    if (index === 0) span.style.transform = 'rotate(45deg) translateY(8px)';
                    if (index === 1) span.style.opacity = '0';
                    if (index === 2) span.style.transform = 'rotate(-45deg) translateY(-8px)';
                } else {
                    span.style.transform = '';
                    span.style.opacity = '';
                }
            });
        });
    }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.navbar') && navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            const spans = hamburger.querySelectorAll('span');
            spans.forEach(span => {
                span.style.transform = '';
                span.style.opacity = '';
            });
        }
    });
});

// =====================
// Auto-dismiss Alerts
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        // Auto dismiss after 5 seconds
        setTimeout(() => {
            alert.style.animation = 'slideOutRight 0.3s ease forwards';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
        
        // Close button functionality
        const closeBtn = alert.querySelector('.close-alert');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                alert.style.animation = 'slideOutRight 0.3s ease forwards';
                setTimeout(() => alert.remove(), 300);
            });
        }
    });
});

// =====================
// Smooth Scroll
// =====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// =====================
// Form Validation Enhancement
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                
                // Re-enable after 3 seconds (in case of validation errors)
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = submitBtn.dataset.originalText || submitBtn.innerHTML;
                }, 3000);
            }
        });
        
        // Store original button text
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.dataset.originalText = submitBtn.innerHTML;
        }
    });
});

// =====================
// Confirm Delete
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('a[href*="delete"], .action-btn.delete');
    
    deleteLinks.forEach(link => {
        if (!link.closest('.delete-form')) {
            link.addEventListener('click', function(e) {
                if (!confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
                    e.preventDefault();
                }
            });
        }
    });
});

// =====================
// Scroll to Top Button
// =====================
document.addEventListener('DOMContentLoaded', function() {
    // Create scroll to top button
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.className = 'scroll-to-top';
    scrollBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 999;
    `;
    
    document.body.appendChild(scrollBtn);
    
    // Show/hide button on scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.style.opacity = '1';
            scrollBtn.style.visibility = 'visible';
        } else {
            scrollBtn.style.opacity = '0';
            scrollBtn.style.visibility = 'hidden';
        }
    });
    
    // Scroll to top on click
    scrollBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Hover effect
    scrollBtn.addEventListener('mouseenter', function() {
        scrollBtn.style.transform = 'translateY(-5px)';
    });
    
    scrollBtn.addEventListener('mouseleave', function() {
        scrollBtn.style.transform = 'translateY(0)';
    });
});

// =====================
// Search Debouncing
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-box input');
    
    if (searchInput) {
        let timeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                this.form.submit();
            }, 500);
        });
    }
});

// =====================
// Task Card Animations
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const taskCards = document.querySelectorAll('.task-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.animation = 'fadeInUp 0.5s ease forwards';
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    taskCards.forEach(card => {
        card.style.opacity = '0';
        observer.observe(card);
    });
});

// =====================
// Date Input Enhancement
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    
    dateInputs.forEach(input => {
        // Set minimum date to today
        if (!input.value) {
            const today = new Date().toISOString().split('T')[0];
            input.min = today;
        }
    });
});

// =====================
// Priority Color Preview
// =====================
document.addEventListener('DOMContentLoaded', function() {
    const prioritySelect = document.querySelector('select[name="priority"]');
    
    if (prioritySelect) {
        const updatePriorityColor = () => {
            prioritySelect.classList.remove('priority-low', 'priority-medium', 'priority-high');
            prioritySelect.classList.add(`priority-${prioritySelect.value}`);
        };
        
        prioritySelect.addEventListener('change', updatePriorityColor);
        updatePriorityColor();
    }
});

// =====================
// Slideout animation for alerts
// =====================
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

console.log('TaskMaster JS Loaded Successfully! 🚀');
