// Animación de aparición al hacer scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Aplicar animación a secciones y tarjetas
document.addEventListener('DOMContentLoaded', () => {
    const fadeElements = document.querySelectorAll('.service-card, .project-card, .section-title, .hero-text');
    
    fadeElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s ease-out';
        observer.observe(el);
    });

    // Sobrescribir estilos inline cuando sea visible
    document.addEventListener('scroll', () => {
        fadeElements.forEach(el => {
            if (el.classList.contains('visible')) {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }
        });
    });
});

// Manejo del formulario de contacto
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = contactForm.querySelector('button');
        const originalText = btn.innerText;
        
        btn.innerText = 'Enviando...';
        btn.disabled = true;
        btn.style.opacity = '0.7';

        // Simulación de envío
        setTimeout(() => {
            btn.innerText = '¡Mensaje Enviado!';
            btn.style.background = '#7ee787';
            btn.style.color = '#0d1117';
            
            contactForm.reset();

            setTimeout(() => {
                btn.innerText = originalText;
                btn.style.background = '';
                btn.style.color = '';
                btn.disabled = false;
                btn.style.opacity = '1';
            }, 3000);
        }, 1500);
    });
}

// Navegación suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
