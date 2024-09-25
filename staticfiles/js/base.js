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

  // Zigzag animation trigger
  const zigzagElements = document.querySelectorAll(".zigzag");
  let resetTimeout;

  // Observer to trigger animations when elements come into view
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const index = Array.from(zigzagElements).indexOf(entry.target);
        entry.target.classList.add("visible");

        if (index % 2 === 0) {
          entry.target.classList.add("slide-in-left");
        } else {
          entry.target.classList.add("slide-in-right");
        }

        // Stop observing once the element is visible
        observer.unobserve(entry.target);
      }
    });
  });

  // Observe each zigzag element for visibility
  zigzagElements.forEach((el) => observer.observe(el));

  const resetZigzagAnimations = () => {
    clearTimeout(resetTimeout);

    resetTimeout = setTimeout(() => {
      zigzagElements.forEach((el) => {
        if (el.classList.contains("visible")) {
          el.classList.remove("visible", "slide-in-left", "slide-in-right");
          observer.observe(el); // Re observe the element for future animations
        }
      });
    }, 250);
  };
});
