function encodeAndDecodeMessages() {
  let textAreas = document.querySelectorAll("textarea");
  let buttons = document.querySelectorAll("button");

  buttons[0].addEventListener("click", encode);
  

  function encode(e) {
    let encodeMessage = "";
    let input = textAreas[0].value;
    for (let index = 0; index < input.length; index++) {
      encodeMessage += String.fromCharCode(input[index].charCodeAt(0) + 1);
    }
    textAreas[1].value = encodeMessage;
    textAreas[0].value = "";
    buttons[1].addEventListener("click", decode);
  }

  function decode(e) {
    let decodeMessage = "";
    let input = textAreas[1].value;
    for (let index = 0; index < input.length; index++) {
      decodeMessage += String.fromCharCode(input[index].charCodeAt(0) - 1);
    }

    textAreas[1].value = decodeMessage;
  }
}
