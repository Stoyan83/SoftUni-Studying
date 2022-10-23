function solve() {
  let textValue = document.getElementById("text").value;
  let convection = document.getElementById("naming-convention").value;

  let result = " ";
  let words = textValue.split(" ");

  if (convection == "Camel Case") {
    for (let i = 0; i < words.length; i++) {
      words[i] = words[i].toLowerCase();
      if (i != 0) {
        words[i] = words[i].charAt(0).toUpperCase() + words[i].substring(1);
      }
    }
  } else if (convection == "Pascal Case") {
    for (let i = 0; i < words.length; i++) {
      words[i] = words[i].toLowerCase();
      words[i] = words[i].charAt(0).toUpperCase() + words[i].substring(1);
    }
  } else {
    return (document.getElementById("result").textContent = "Error!");
  }

  result = words.join("");
  document.getElementById("result").textContent = result;
}
