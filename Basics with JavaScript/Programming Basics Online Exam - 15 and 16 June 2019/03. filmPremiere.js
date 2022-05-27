function filmPremiere(input) {
    let name = input[0];
    let snacks = input[1];
    let numberOfTickets = Number(input[2]);

    const prices = {
        "John Wick": { "Drink": 12, "Popcorn": 15, "Menu":19 },
        "Star Wars": { "Drink": 18, "Popcorn": 25, "Menu": 30 },
        "Jumanji": { "Drink": 9, "Popcorn": 11, "Menu": 14 }
    };

    let total = prices[name][snacks] * numberOfTickets;

    if (name == "Star Wars" && numberOfTickets >= 4) {
        total = total * 0.7
    } if (name == "Jumanji" && numberOfTickets === 2) {
       total = total * 0.85
    }

    console.log(`Your bill is ${total.toFixed(2)} leva.`);
}

filmPremiere(["Star Wars",
"Drink",
"10"])