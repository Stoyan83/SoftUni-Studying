function movieProfit(input) {
    let name = input[0];
    let days = Number(input[1]);
    let numberOfTickets = Number(input[2]);
    let ticketPrice = Number(input[3]);
    let cinemaPercentage = Number(input[4]);

    let totalProfit = days * numberOfTickets * ticketPrice;
    let total = totalProfit - totalProfit * cinemaPercentage / 100

    console.log(`The profit from the movie ${name} is ${total.toFixed(2)} lv.`);
}

movieProfit(["The Programmer",
"20",
"500",
"7.50",
"7"]);