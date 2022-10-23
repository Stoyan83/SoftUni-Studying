function notify(message) {
  let messageEl = document.getElementById("notification");
  messageEl.textContent = message;
  messageEl.style.display = "block";
  messageEl.addEventListener("click", onClick);

  function onClick() {
    messageEl.style.display = "none";    
  }
}
