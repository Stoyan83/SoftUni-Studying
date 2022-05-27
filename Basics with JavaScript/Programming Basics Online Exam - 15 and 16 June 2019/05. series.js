function series(input) {

    let budget = Number(input[0]);
    let numberOfSerials = input[1];
    let index = 2;

    for (let i = 0; i < numberOfSerials; i++) {
        let name = input[index++]
        let price = Number(input[index++])
        if (name === "Thrones") {
            price *= 0.50
        } if (name === "Lucifer") {
            price *= 0.6
        }if (name === "Protector") {
            price *= 0.7
        } if (name === "TotalDrama") {
            price *= 0.8
        } if (name === "Area") {
            price *= 0.9
        }
        budget -= price
        
    }

    if (budget >= 0) {
        console.log(`You bought all the series and left with ${budget.toFixed(2)} lv.`);
    } else {
        console.log(`You need ${Math.abs(budget).toFixed(2)} lv. more to buy the series!`);
    }
}


series(["10",
"3",
"Thrones",
"5",
"Riverdale",
"5",
"Gotham",
"2"])