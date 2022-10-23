function search() {
  let listElements = document.querySelectorAll("ul#towns li");
  let resultValue = document.getElementById("result");
  let searchText = document.getElementById("searchText").value;

  let matches = 0;

  for (let el of listElements) {
    let text = el.textContent;

    if (text.match(searchText)) {
      matches++;
      el.style.fontWeight = "bold";
      el.style.textDecoration = "underline";
    } else {
      el.style.fontWeight = "normal";
      el.style.textDecoration = "none";
    }
  }

  resultValue.textContent = `${matches} matches found`;
}
