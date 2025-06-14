// admissions.js

document.addEventListener('DOMContentLoaded', () => {
  const admissionBtn = document.getElementById('admissionProcessBtn');
  const applyBtn = document.getElementById('applyOnlineBtn');

  if (admissionBtn) {
    admissionBtn.addEventListener('mouseenter', () => {
      admissionBtn.textContent = 'Learn About the Process';
    });
    admissionBtn.addEventListener('mouseleave', () => {
      admissionBtn.textContent = 'Admission Process';
    });
  }

  if (applyBtn) {
    applyBtn.addEventListener('mouseenter', () => {
      applyBtn.textContent = 'Start Your Application';
    });
    applyBtn.addEventListener('mouseleave', () => {
      applyBtn.textContent = 'Apply Online';
    });
  }

  // Bootstrap 5 form validation
  (() => {
    'use strict';
    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  })();
});
