function repainting(input) {
    let cover = 1.5;
    let paint = 14.5;
    let tinnerPaint = 5;
    let coverNeeded = Number(input[0]);
    let paintNeeded = Number(input[1]);
    let litersTinnerPaint = Number(input[2]);
    let hours = Number(input[3]);
    let total = paintNeeded * 1.1 * paint + ((coverNeeded + 2) * cover) + (litersTinnerPaint * tinnerPaint) + 0.4;
    let pricePerHour = total * 0.3;
    let totalWithWork = total + hours * pricePerHour ;
    console.log(totalWithWork);
}
repainting(["10 ",
"11 ",
"4 ",
"8 "]
);