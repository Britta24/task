const params = new URLSearchParams(window.location.search);
const role = params.get("role");

function register() {
  if (!email.value || !password.value) return alert("Fill all fields");

  localStorage.setItem(role + "_user", JSON.stringify({
    email: email.value,
    password: password.value
  }));

  alert("Registered successfully");
  window.location.href = `login.html?role=${role}`;
}

function login() {
  const user = JSON.parse(localStorage.getItem(role + "_user"));

  if (!user || user.email !== email.value || user.password !== password.value)
    return alert("Invalid credentials");

  localStorage.setItem("loggedIn", email.value);
  localStorage.setItem("role", role);

  window.location.href = role + ".html";
}