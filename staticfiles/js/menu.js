document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript file loaded.");

  const modals = document.querySelectorAll('.modal');
  modals.forEach(modal => {
    modal.addEventListener('show.bs.modal', function () {
      const modalBody = modal.querySelector('.modal-body');
      modalBody.style.animation = 'fadeInUp 0.5s ease-in-out';
    });
  });

  const categoryButtons = document.querySelectorAll('.btn-category');
  categoryButtons.forEach(button => {
    button.addEventListener('mouseover', function () {
      this.style.transition = 'all 0.3s ease';
      this.style.transform = 'scale(1.05)';
    });
    button.addEventListener('mouseout', function () {
      this.style.transform = 'scale(1)';
    });
  });
});
