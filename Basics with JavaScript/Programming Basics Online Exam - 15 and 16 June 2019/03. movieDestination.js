function movieDestination(input) {
    let budget = Number(input[0]);
    let destination = input[1];
    let season = input[2]
    days = Number(input[3]);

    const oneDayPrice = {"Dubai" : {"Winter" : 45000, "Summer": 40000},
     "Sofia": {"Winter" : 17000, "Summer": 12500}, "London" : {"Winter" : 24000, "Summer": 20250}};

    let total = oneDayPrice[destination][season] * days;

    if (destination == "Dubai") {
        total = total * 0.7
    } else if (destination == "Sofia") {
       total = total * 1.25
    }
    
    if (budget >= total) {
        console.log(`The budget for the movie is enough! We have ${(budget - total).toFixed(2)} leva left!`);
    } else {
        console.log(`The director needs ${(total - budget).toFixed(2)} leva more!`);
    }


}


movieDestination(["1500000",
"Sofia",
"Summer",
"13"])