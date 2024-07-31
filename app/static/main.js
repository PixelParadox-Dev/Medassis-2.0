function wholecursor() {
  const cursor = document.getElementById("cursorelement");
  let isScrolling;
  let lastMouseX = 0;
  let lastMouseY = 0;

  // Helper function to update cursor position
  const updateCursorPosition = (e) => {
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
    gsap.to(cursor, {
      x: lastMouseX,
      y: lastMouseY + window.scrollY,
      duration: 0.5,
      ease: "power2.out",
    });
  };

  // Mousemove event to track the cursor position
  document.addEventListener("mousemove", updateCursorPosition);

  // Mouseenter event to show the cursor
  document.addEventListener("mouseenter", () => {
    gsap.to(cursor, {
      scale: 1,
      opacity: 1,
      duration: 0.3,
    });
  });

  // Mouseleave event to hide the cursor
  document.addEventListener("mouseleave", () => {
    gsap.to(cursor, {
      scale: 0,
      opacity: 0,
      duration: 0.3,
    });
  });

  // Scroll event to hide the cursor while scrolling
  document.addEventListener("scroll", () => {
    // Hide cursor on scroll
    gsap.to(cursor, {
      opacity: 0,
      duration: 0.3,
    });

    // Clear previous timeout if scrolling continues
    window.clearTimeout(isScrolling);

    // Set a timeout to run after scrolling ends
    isScrolling = setTimeout(() => {
      // Update cursor position to the last recorded mouse position
      gsap.to(cursor, {
        x: lastMouseX,
        y: lastMouseY + window.scrollY,
        opacity: 1,
        duration: 0.3,
        ease: "power2.out",
      });
    }, 150); // Adjust the timeout duration as needed
  });
}

wholecursor();

function toggleNav() {
  const navContent = document.querySelector(".nav-contentmob");
  const navIcon = document.querySelector(".butnav");

  if (navContent.style.display === "block") {
    navContent.style.display = "none";
    navIcon.classList.remove("fa-times");
    navIcon.classList.add("fa-bars");
  } else {
    navContent.style.display = "block";
    navIcon.classList.remove("fa-bars");
    navIcon.classList.add("fa-times");
  }
}

const swiper = new Swiper(".swiper", {
  // Optional parameters
  direction: "horizontal",
  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  // And if we need scrollbar
  
});

