// Плавное появление элементов при прокрутке
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.2 });
  
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
  });