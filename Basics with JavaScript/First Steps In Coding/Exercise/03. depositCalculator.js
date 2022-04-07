function deposit(input) {
    let depositAmount = Number(input[0]);
    let termOfDeposit = Number(input[1]);
    let annualInterest = Number(input[2]);
    let totalSum = depositAmount + termOfDeposit * ((depositAmount * annualInterest/100) / 12);
    console.log(totalSum)
}

deposit(["2350",
"6 ",
"7 "]);