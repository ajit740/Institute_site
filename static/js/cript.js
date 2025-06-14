// Toggle mobile menu visibility
document.addEventListener('DOMContentLoaded', function () {
  const nav = document.querySelector('nav');
  const toggleButton = document.createElement('button');
  toggleButton.textContent = 'Menu';
  toggleButton.style.display = 'none'; // Hide by default
  toggleButton.style.background = '#004080';
  toggleButton.style.color = 'white';
  toggleButton.style.border = 'none';
  toggleButton.style.padding = '8px 12px';
  toggleButton.style.cursor = 'pointer';

  nav.insertBefore(toggleButton, nav.firstChild);

  // Show toggle button only on small screens
  function checkWidth() {
    if (window.innerWidth < 600) {
      toggleButton.style.display = 'inline-block';
      nav.querySelectorAll('a').forEach(link => {
        link.style.display = 'none';
      });
    } else {
      toggleButton.style.display = 'none';
      nav.querySelectorAll('a').forEach(link => {
        link.style.display = 'inline-block';
      });
    }
  }

  checkWidth();

  window.addEventListener('resize', checkWidth);

  toggleButton.addEventListener('click', () => {
    nav.querySelectorAll('a').forEach(link => {
      if (link.style.display === 'none') {
        link.style.display = 'inline-block';
      } else {
        link.style.display = 'none';
      }
    });
  });

  // Smooth scroll for nav links
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      if (targetId.startsWith('#')) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
          });
        }
      } else {
        // Normal navigation for external/internal pages
        window.location.href = targetId;
      }
    });
  });
});
