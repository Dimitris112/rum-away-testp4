document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("custom-404-active");

  gsap.from("#custom-404-title", {
    duration: 1.5,
    y: -100,
    opacity: 0,
    ease: "bounce.out",
  });

  gsap.from("#custom-404-paragraph-1", {
    duration: 1,
    delay: 0.5,
    y: 30,
    opacity: 0,
    ease: "power2.out",
  });
  gsap.from("#custom-404-paragraph-2", {
    duration: 1,
    delay: 1,
    y: 30,
    opacity: 0,
    ease: "power2.out",
  });
  gsap.from("#custom-404-paragraph-3", {
    duration: 1,
    delay: 1.5,
    y: 30,
    opacity: 0,
    ease: "power2.out",
  });

  gsap.from(".custom-btn-404", {
    duration: 1,
    delay: 2,
    opacity: 0,
    y: 20,
    stagger: 0.2,
    ease: "elastic.out(1, 0.5)",
    rotation: 10, // Add a rotation effect
  });

  gsap.to(".custom-btn-404", {
    duration: 1.5,
    scale: 1.05,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut",
  });
});

// remove class if leave 404
window.addEventListener("beforeunload", () => {
  document.body.classList.remove("custom-404-active");
});
