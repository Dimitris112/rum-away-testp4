document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navbar");
  const navLinks = document.querySelectorAll(".nav-link");
  let lastScrollTop = 0;

  // Smooth scrolling
  navLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");
      if (targetId.startsWith("#")) {
        e.preventDefault();
        const target = document.querySelector(targetId);
        if (target) {
          window.scrollTo({
            top: target.offsetTop,
            behavior: "smooth",
          });
        }
      }
    });
  });

  const debounce = (func, wait) => {
    let timeout;
    return function () {
      const context = this,
        args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(context, args), wait);
    };
  };

  const handleScroll = () => {
    const currentScroll =
      window.pageYOffset || document.documentElement.scrollTop;

    navbar.classList.toggle("scrolled", currentScroll > 50);

    // Show navbar when scrolling up or at the top of the page
    if (currentScroll < lastScrollTop) {
      navbar.style.top = "0"; // Show navbar
      navbar.classList.add("visible");
    } else {
      // Hide navbar when scrolling down
      navbar.style.top = `-${navbar.offsetHeight}px`;
      navbar.classList.remove("visible");
    }

    navLinks.forEach((link) => {
      const targetId = link.getAttribute("href");
      if (targetId.startsWith("#")) {
        const target = document.querySelector(targetId);
        const bounding = target.getBoundingClientRect();
        link.classList.toggle(
          "active",
          bounding.top >= 0 && bounding.top < window.innerHeight
        );
      }
    });

    lastScrollTop = Math.max(currentScroll, 0); // For Mobile or negative scrolling
  };

  window.addEventListener("scroll", debounce(handleScroll, 100));
});
