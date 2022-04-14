function coffee(input) {
    const menu ={"Espresso":{"Without":0.9, "Normal":1,"Extra":1.2},
    "Cappuccino":{"Without":1, "Normal":1.2,"Extra":1.6},
    "Tea":{"Without":0.5, "Normal":0.6,"Extra":0.7}}

    let price = menu[input[0]][input[1]];
    let quantity = Number(input[2])
    let total = quantity * price
    if (input[1] === "Without") {
        total *= 0.65;
    }if (input[0] === "Espresso" && quantity >= 5) {
        total *= 0.75;
    } if (total > 15) {
        total *= 0.8;
    }

    console.log(`You bought ${quantity} cups of ${input[0]} for ${(total).toFixed(2)} lv.`);
}

coffee(["Cappuccino",
"Normal",
"13"])