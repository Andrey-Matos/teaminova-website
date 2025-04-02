document.addEventListener("DOMContentLoaded", function () {
  toggleAuth(document.getElementById("registerBtn"), "register");
});

function clearMessages() {
  document
    .querySelectorAll(".error-message")
    .forEach((error) => error.remove());
}

function toggleAuth(selected, mode) {
  clearMessages();

  document
    .querySelectorAll(".toggle-btn")
    .forEach((btn) => btn.classList.remove("active"));
  selected.classList.add("active");

  const isLogin = mode === "login";
  document.getElementById("nameField").classList.toggle("hidden", isLogin);
  document
    .getElementById("confirmPasswordField")
    .classList.toggle("hidden", isLogin);
  document
    .getElementById("forgotPassword")
    .classList.toggle("hidden", !isLogin);

  document.querySelector(".enter").textContent = isLogin ? "Login" : "Register";
  document.getElementById("authForm").action = isLogin
    ? "/accounts/login/"
    : "/accounts/register_user/";
}

document.addEventListener("click", function (event) {
  if (event.target.classList.contains("toggle-password")) {
    const passwordField = document.getElementById(event.target.dataset.target);
    passwordField.type =
      passwordField.type === "password" ? "text" : "password";
    event.target.classList.toggle("fa-eye");
    event.target.classList.toggle("fa-eye-slash");
  }
});
