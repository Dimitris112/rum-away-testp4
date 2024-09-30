import "../static/js/404";

describe("Smooth scrolling functionality", () => {
  let link;

  beforeEach(() => {
    document.body.innerHTML = `
          <div class="navbar"></div>
          <a href="#section1" class="nav-link">Section 1</a>
          <div id="section1"></div>
        `;
    link = document.querySelector(".nav-link");
    window.scrollTo = jest.fn();

    // adding event listener for smooth scrolling
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

  test("should scroll to the correct section on click", () => {
    link.click();
    expect(window.scrollTo).toHaveBeenCalledWith({
      top: expect.any(Number),
      behavior: "smooth",
    });
  });
});

describe("Navbar visibility on scroll", () => {
  let navbar;
  let handleScroll;

  beforeEach(() => {
    document.body.innerHTML = `
          <div class="navbar"></div>
        `;
    navbar = document.querySelector(".navbar");
    handleScroll = () => {
      const currentScroll =
        window.pageYOffset || document.documentElement.scrollTop;

      if (currentScroll > 50) {
        navbar.classList.add("scrolled");
      }

      if (currentScroll < 50) {
        navbar.style.top = "0"; // showing navbar
        navbar.classList.add("visible");
      } else {
        navbar.style.top = `-${navbar.offsetHeight}px`; // hiding navbar
        navbar.classList.remove("visible");
      }
    };
  });

  test("should hide navbar when scrolling down", () => {
    window.pageYOffset = 100; // scrolling down
    handleScroll();

    expect(navbar.style.top).toBe(`-${navbar.offsetHeight}px`);
  });

  test("should show navbar when scrolling up", () => {
    window.pageYOffset = 0; // scrolling up
    handleScroll();

    expect(navbar.style.top).toBe("0px");
    expect(navbar.classList.contains("visible")).toBe(true);
  });
});

describe("Zigzag animation triggering", () => {
  let observer, zigzagElements;

  beforeEach(() => {
    document.body.innerHTML = `
        <div class="zigzag"></div>
        <div class="zigzag"></div>
      `;
    zigzagElements = document.querySelectorAll(".zigzag");
    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = Array.from(zigzagElements).indexOf(entry.target);
          entry.target.classList.add("visible");

          if (index % 2 === 0) {
            entry.target.classList.add("slide-in-left");
          } else {
            entry.target.classList.add("slide-in-right");
          }
        }
      });
    });
  });

  test("should add correct classes for zigzag animations", () => {
    zigzagElements.forEach((el, index) => {
      const entry = { isIntersecting: true, target: el };
      observer.callback([entry]);

      expect(el.classList.contains("visible")).toBe(true);
      if (index % 2 === 0) {
        expect(el.classList.contains("slide-in-left")).toBe(true);
      } else {
        expect(el.classList.contains("slide-in-right")).toBe(true);
      }
    });
  });
});

global.IntersectionObserver = class IntersectionObserver {
  constructor(callback) {
    this.callback = callback;
  }

  observe() {
    // observing
  }

  unobserve() {
    // unobserving
  }
};
describe("Reset zigzag animations", () => {
  let resetTimeout, zigzagElements;

  beforeEach(() => {
    jest.useFakeTimers();
    document.body.innerHTML = `
        <div class="zigzag visible slide-in-left"></div>
        <div class="zigzag visible slide-in-right"></div>
      `;
    zigzagElements = document.querySelectorAll(".zigzag");
  });

  test("should reset animations after timeout", () => {
    resetTimeout = setTimeout(() => {
      zigzagElements.forEach((el) => {
        el.classList.remove("visible", "slide-in-left", "slide-in-right");
      });
    }, 250);

    jest.runAllTimers();

    zigzagElements.forEach((el) => {
      expect(el.classList.contains("visible")).toBe(false);
      expect(el.classList.contains("slide-in-left")).toBe(false);
      expect(el.classList.contains("slide-in-right")).toBe(false);
    });
  });
});
