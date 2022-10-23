function subtract() {
  let num1 = document.getElementById("firstNumber").value;
  let num2 = document.getElementById("secondNumber").value;
  let resultValue = document.getElementById("result");
  resultValue.textContent = Number(num1) - Number(num2);
}
