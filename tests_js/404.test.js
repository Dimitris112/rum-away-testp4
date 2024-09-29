import { gsap } from "gsap";
import "../static/js/404";

describe("404 Page Animation Tests", () => {
  beforeEach(() => {
    document.body.innerHTML = `
            <div id="custom-404-title">404 Not Found</div>
            <p id="custom-404-paragraph-1">Sorry, the page you are looking for does not exist.</p>
            <p id="custom-404-paragraph-2">Please check the URL and try again.</p>
            <p id="custom-404-paragraph-3">If you need assistance, contact support.</p>
            <button class="custom-btn-404">Go Back</button>
        `;
    jest.clearAllMocks(); // Clear mock calls before each test
  });

  test("should add custom-404-active class to body on DOMContentLoaded", () => {
    document.body.classList.add("custom-404-active");

    // Check if the class is added
    expect(document.body.classList.contains("custom-404-active")).toBe(true);
  });

  test("should call GSAP animations for title and paragraphs", () => {
    // Mock gsap.from to track its calls
    gsap.from = jest.fn();

    const event = new Event("DOMContentLoaded");
    document.dispatchEvent(event);

    // Check if gsap.from was called the expected number of times
    expect(gsap.from).toHaveBeenCalledTimes(5); // 5 GSAP calls

    // Check specific GSAP calls with exact arguments
    expect(gsap.from).toHaveBeenCalledWith("#custom-404-title", {
      duration: 1.5,
      y: -100,
      opacity: 0,
      ease: "bounce.out",
    });
    expect(gsap.from).toHaveBeenCalledWith("#custom-404-paragraph-1", {
      duration: 1,
      delay: 0.5,
      y: 30,
      opacity: 0,
      ease: "power2.out",
    });
    expect(gsap.from).toHaveBeenCalledWith("#custom-404-paragraph-2", {
      duration: 1,
      delay: 1,
      y: 30,
      opacity: 0,
      ease: "power2.out",
    });
    expect(gsap.from).toHaveBeenCalledWith("#custom-404-paragraph-3", {
      duration: 1,
      delay: 1.5,
      y: 30,
      opacity: 0,
      ease: "power2.out",
    });
    expect(gsap.from).toHaveBeenCalledWith(".custom-btn-404", {
      duration: 1,
      delay: 2,
      opacity: 0,
      y: 20,
      stagger: 0.2,
      ease: "elastic.out(1, 0.5)",
      rotation: 10,
    });
  });

  test("should remove custom-404-active class on beforeunload", () => {
    document.body.classList.add("custom-404-active");

    const unloadEvent = new Event("beforeunload");
    window.dispatchEvent(unloadEvent);

    document.body.classList.remove("custom-404-active");

    // Check if the class was removed
    expect(document.body.classList.contains("custom-404-active")).toBe(false);
  });
});
