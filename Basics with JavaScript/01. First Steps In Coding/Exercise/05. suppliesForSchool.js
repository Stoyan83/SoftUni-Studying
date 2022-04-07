function studyMaterials(input) {
    let packPens = 5.8;
    let packTipPens = 7.2;
    let detergent = 1.2;
    let numberOfPackPens = Number(input[0]);
    let numberOfPackTipPens = Number(input[1]);
    let litersDetergent = Number(input[2]);
    let discount = Number(input[3]) / 100;
    let total = (numberOfPackPens * packPens + numberOfPackTipPens * packTipPens + litersDetergent * detergent);
    let totalPlusDiscount = total - total * discount;
    console.log(totalPlusDiscount);
}   

studyMaterials(
    ["4 ",
    "2 ",
    "5 ",
    "13 "]
    );