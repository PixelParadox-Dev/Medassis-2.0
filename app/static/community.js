document.addEventListener("DOMContentLoaded", function () {
  // Load messages from localStorage when the page is loaded
  loadMessages();
});

document.getElementById("send-button").addEventListener("click", function () {
  sendMessage();
});

document
  .getElementById("chat-input")
  .addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

document.getElementById("dark-mode").addEventListener("change", function () {
  document.body.classList.toggle("dark-mode", this.checked);
});

function sendMessage() {
  const inputField = document.getElementById("chat-input");
  const message = inputField.value.trim();

  if (message !== "") {
    appendMessage(message, "user");
    inputField.value = "";
    saveMessages(); // Save messages to localStorage
    simulateBotResponse();
  }
}

function appendMessage(message, sender) {
  const messageContainer = document.createElement("div");
  messageContainer.classList.add("message", sender);

  const messageText = document.createElement("span");
  messageText.textContent = message;

  const timestamp = document.createElement("span");
  timestamp.classList.add("timestamp");
  timestamp.textContent = formatAMPM(new Date());

  messageContainer.appendChild(messageText);
  messageContainer.appendChild(timestamp);

  const chatWindow = document.getElementById("chat-window");
  chatWindow.appendChild(messageContainer);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function simulateBotResponse() {
  setTimeout(() => {
    appendMessage("This is a bot response.", "bot");
    saveMessages(); // Save messages to localStorage
  }, 1000);
}

function formatAMPM(date) {
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? "0" + minutes : minutes;
  const strTime = hours + ":" + minutes + " " + ampm;
  return strTime;
}

function saveMessages() {
  const chatWindow = document.getElementById("chat-window");
  localStorage.setItem("messages", chatWindow.innerHTML);
}

function loadMessages() {
  const savedMessages = localStorage.getItem("messages");
  if (savedMessages) {
    const chatWindow = document.getElementById("chat-window");
    chatWindow.innerHTML = savedMessages;
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
}
