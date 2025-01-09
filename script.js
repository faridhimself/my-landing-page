// Mobile navigation toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.querySelector('.nav-links');

navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
        navLinks.classList.remove('active');
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        navLinks.classList.remove('active');

        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Scroll animations
const animateElements = document.querySelectorAll('.animate-on-scroll');

const animateOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.8;

    animateElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;

        if (elementTop < triggerBottom) {
            element.classList.add('active');
        }
    });
};

// Initial check for elements in view
animateOnScroll();

// Listen for scroll events
window.addEventListener('scroll', animateOnScroll);

// Active navigation link on scroll
const sections = document.querySelectorAll('section');
const navItems = document.querySelectorAll('.nav-links a');

const updateActiveNavLink = () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.pageYOffset >= sectionTop - 150) {
            current = section.getAttribute('id');
        }
    });

    navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href').slice(1) === current) {
            item.classList.add('active');
        }
    });
};

window.addEventListener('scroll', updateActiveNavLink);

// Form submission
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Add your form submission logic here
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);
        
        // For demonstration, log the form data
        console.log('Form submitted:', data);
        
        // Show success message
        const button = contactForm.querySelector('button');
        const originalText = button.textContent;
        button.textContent = 'Message Sent!';
        button.style.backgroundColor = 'var(--success-color)';
        
        // Reset form
        contactForm.reset();
        
        // Reset button after 3 seconds
        setTimeout(() => {
            button.textContent = originalText;
            button.style.backgroundColor = '';
        }, 3000);
    });
}

// Animated counter for statistics
const animateValue = (element, start, end, duration) => {
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= end) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current).toLocaleString();
    }, 16);
};

// Animate statistics when they come into view
const statsElements = document.querySelectorAll('.analytics-card .stat');
let animated = false;

const animateStats = () => {
    if (animated) return;
    
    const cards = document.querySelectorAll('.analytics-card');
    const triggerBottom = window.innerHeight * 0.8;
    
    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        if (cardTop < triggerBottom) {
            const statElement = card.querySelector('.stat');
            const value = statElement.textContent;
            const endValue = parseInt(value.replace(/[^0-9]/g, ''));
            animateValue(statElement, 0, endValue, 2000);
            animated = true;
        }
    });
};

window.addEventListener('scroll', animateStats);
