function basketball(input) {
    let annualTax = Number(input[0]);
    let snickers = annualTax * 0.6;
    let clothes = snickers * 0.8;
    let ball = clothes / 4;
    let accessories = ball / 5;
    let total = annualTax + snickers + clothes + ball + accessories;
    console.log(total);
}

basketball(["365 "]);