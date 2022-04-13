function snooker(input) {
    let round = input[0];
    let ticketType = input[1];
    let countTicket = Number(input[2]);
    let picture = input[3];

    const tourney = {
        "Final": { "Standard": 110.10, "Premium": 160.66, "VIP": 400 },
        "Semi final": { "Standard": 75.88, "Premium": 125.22, "VIP": 300.40 },
        "Quarter final": { "Standard": 55.50, "Premium": 105.2, "VIP": 118.90 }
    }

    let total = 0;
    let ticketPrice = tourney[round][ticketType];
    total = ticketPrice * countTicket;
    let pricePicture = 0;

    if (picture === "Y") {
        pricePicture = 40;
    }
    if (total > 4000) {
        pricePicture = 0;
        total *= 0.75
    } else if (total > 2500) {
        total *= 0.9;
    }
    total += countTicket * pricePicture;

    console.log(total.toFixed(2));
}

snooker(["Final",
    "Premium",
    "25",
    "Y"])