/* ============================================================
   SIGMA ECOBUILD & INNOVATION — SHARED JAVASCRIPT
   Dynamic Multi-Page Website
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {

  // ===== LOADING OVERLAY =====
  const loadingOverlay = document.querySelector('.loading-overlay');
  if (loadingOverlay) {
    window.addEventListener('load', function() {
      setTimeout(() => {
        loadingOverlay.classList.add('hidden');
      }, 300);
    });
  }

  // ===== NAVBAR SCROLL EFFECT =====
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // ===== BACK TO TOP BUTTON =====
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 500) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    });
    backToTop.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ===== SCROLL ANIMATIONS =====
  const animateElements = document.querySelectorAll('.animate-on-scroll');

  const observerOptions = {
    root: null,
    rootMargin: '0px',
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

  animateElements.forEach(el => observer.observe(el));

  // ===== STAT COUNTER ANIMATION =====
  const statNumbers = document.querySelectorAll('.stat-number[data-count]');

  const countObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const countTo = parseInt(target.getAttribute('data-count'));
        const duration = 2000;
        const startTime = performance.now();

        function updateCount(currentTime) {
          const elapsed = currentTime - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeOut = 1 - Math.pow(1 - progress, 3);
          const current = Math.floor(easeOut * countTo);

          target.textContent = current.toLocaleString() + (target.getAttribute('data-suffix') || '');

          if (progress < 1) {
            requestAnimationFrame(updateCount);
          } else {
            target.textContent = countTo.toLocaleString() + (target.getAttribute('data-suffix') || '');
          }
        }

        requestAnimationFrame(updateCount);
        countObserver.unobserve(target);
      }
    });
  }, { threshold: 0.5 });

  statNumbers.forEach(el => countObserver.observe(el));

  // ===== TABS =====
  const tabContainers = document.querySelectorAll('.tab-container');
  tabContainers.forEach(container => {
    const buttons = container.querySelectorAll('.tab-btn');
    const panels = container.querySelectorAll('.tab-panel');

    buttons.forEach(btn => {
      btn.addEventListener('click', function() {
        const target = this.getAttribute('data-tab');

        buttons.forEach(b => b.classList.remove('active'));
        panels.forEach(p => p.classList.remove('active'));

        this.classList.add('active');
        container.querySelector('#' + target).classList.add('active');
      });
    });
  });

  // ===== ACCORDION =====
  const accordionItems = document.querySelectorAll('.accordion-item');
  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    if (header) {
      header.addEventListener('click', function() {
        const isOpen = item.classList.contains('open');

        // Close all others (optional - remove for multiple open)
        accordionItems.forEach(other => {
          if (other !== item) other.classList.remove('open');
        });

        item.classList.toggle('open');
      });
    }
  });

  // ===== MOBILE MENU CLOSE ON LINK CLICK =====
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.querySelectorAll('.nav-links a');
  if (navToggle) {
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navToggle.checked = false;
      });
    });
  }

  // ===== SMOOTH SCROLL FOR ANCHOR LINKS =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // ===== FORM VALIDATION =====
  const forms = document.querySelectorAll('form[data-validate]');
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      let isValid = true;
      const requiredFields = form.querySelectorAll('[required]');

      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.style.borderColor = '#c62828';

          // Shake animation
          field.style.animation = 'shake 0.5s ease';
          setTimeout(() => {
            field.style.animation = '';
          }, 500);
        } else {
          field.style.borderColor = '';
        }
      });

      if (!isValid) {
        e.preventDefault();
      }
    });
  });

  // ===== NEWSLETTER FORM =====
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const email = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button[type="submit"]');

      if (email && email.value.trim()) {
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-check"></i> Subscribed!';
        btn.style.background = 'var(--sigma-green)';
        email.value = '';

        setTimeout(() => {
          btn.innerHTML = originalText;
          btn.style.background = '';
        }, 3000);
      }
    });
  });

  // ===== PROJECT FILTER (if exists) =====
  const filterButtons = document.querySelectorAll('.filter-btn');
  const filterItems = document.querySelectorAll('.filter-item');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const filter = this.getAttribute('data-filter');

      filterButtons.forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      filterItems.forEach(item => {
        if (filter === 'all' || item.getAttribute('data-category') === filter) {
          item.style.display = '';
          item.style.animation = 'fadeInUp 0.4s ease';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // ===== TESTIMONIAL SLIDER (if exists) =====
  const testimonialSlider = document.querySelector('.testimonial-slider');
  if (testimonialSlider) {
    const slides = testimonialSlider.querySelectorAll('.testimonial-slide');
    const prevBtn = testimonialSlider.querySelector('.slider-prev');
    const nextBtn = testimonialSlider.querySelector('.slider-next');
    let currentSlide = 0;

    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
        if (i === index) slide.style.animation = 'fadeIn 0.5s ease';
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
      });
    }

    // Auto-advance
    setInterval(() => {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }, 6000);

    showSlide(0);
  }

  // ===== CURRENT YEAR IN FOOTER =====
  const yearElements = document.querySelectorAll('.current-year');
  yearElements.forEach(el => {
    el.textContent = new Date().getFullYear();
  });

});

// ===== SHAKE ANIMATION KEYFRAMES (injected via JS for forms) =====
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-5px); }
    40% { transform: translateX(5px); }
    60% { transform: translateX(-5px); }
    80% { transform: translateX(5px); }
  }
`;
document.head.appendChild(shakeStyle);
