function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  let rows = document.querySelectorAll("tbody tr");
  let inputValue = document.getElementById("searchField");

  function onClick() {
    for (let row of rows) {
      row.className = "";
      if (inputValue.value != '' && row.innerHTML.includes(inputValue.value)) {
        row.className = "select";
      }
    }
    inputValue.value = "";
  }
}
