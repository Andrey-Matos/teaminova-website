document.addEventListener("DOMContentLoaded", function () {
  clearMessages();
  loginOrRegister();
});

let switchInput = document.querySelector(".sswitch input");
let nameField = document.getElementById("nameField");
let confirmPassword = document.getElementById("confirmPassword");
let password = document.getElementById("password");
let title = document.getElementById("title");
let enterButton = document.querySelector(".enter");
let form = document.getElementById("signupForm");

function loginOrRegister() {
  if (enterButton.innerHTML === "Register") {
    form.action = "{% url 'register_user' %}";
  } else {
    form.action = "{% url 'login' %}";
  }
}

function clearMessages() {
  let messages = document.getElementById("messages");
  messages.innerHTML = "";
}

switchInput.addEventListener("change", function () {
  clearMessages();
  if (this.checked) {
    nameField.style.maxHeight = "0";
    confirmPassword.parentElement.style.maxHeight = "0";
    title.innerHTML = "Sign in";
    enterButton.innerHTML = "Login";
  } else {
    nameField.style.maxHeight = "60px";
    confirmPassword.parentElement.style.maxHeight = "60px";
    title.innerHTML = "Sign up";
    enterButton.innerHTML = "Register";
  }
  loginOrRegister();
});

document
  .querySelectorAll("#toggle-password, #toggle-confirm-password")
  .forEach((icon) => {
    icon.addEventListener("click", function () {
      let targetId = this.getAttribute("data-target");
      let passwordField = document.getElementById(targetId);
      if (passwordField.type === "password") {
        passwordField.type = "text";
        this.classList.remove("fa-eye");
        this.classList.add("fa-eye-slash");
      } else {
        passwordField.type = "password";
        this.classList.remove("fa-eye-slash");
        this.classList.add("fa-eye");
      }
    });
  });
