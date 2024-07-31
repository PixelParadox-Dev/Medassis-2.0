const texts = ["companion.", "assistant", "helper","guide"];
let currentIndex = 0;

document.addEventListener("DOMContentLoaded", () => {
  const textElement = document.querySelector(".textchange");

  function changeText() {
    textElement.textContent = texts[currentIndex];
    currentIndex = (currentIndex + 1) % texts.length;
  }

  changeText(); // Call immediately to set the initial text
  setInterval(changeText, 3000);
});

// function sayHello() {
//   console.log('Hello, World!');
// }

// // Call sayHello every 2 seconds
// setInterval(sayHello, 2000); // 2000 milliseconds = 2 seconds
