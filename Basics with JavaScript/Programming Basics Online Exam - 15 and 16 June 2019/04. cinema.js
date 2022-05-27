function cinema(input) {
    let index = 0;
    let holeCapacity = Number(input[index]);
    index++;
    let currentHoleCapacity = holeCapacity
    const ticketPrice = 5;
    let currentPeople = 0;
    let income = 0;
    let full = false;

    command = Number(input[index++])
    while (command !== "Movie time!") {

        let peopleEntered = Number(command)


        holeCapacity -= peopleEntered
        currentPeople += peopleEntered
        income += peopleEntered * ticketPrice
        if (currentHoleCapacity < currentPeople) {
            holeCapacity += peopleEntered
            currentPeople -= peopleEntered
            income -= peopleEntered * ticketPrice
                full = true
                break
            }
    
        if (peopleEntered % 3 === 0) {
            income -= 5
        }

  


        command = input[index++]
    }

    if (full) {
        console.log(`The cinema is full.`);
        console.log(`Cinema income - ${income} lv.`);

    } else {

        console.log(`There are ${holeCapacity} seats left in the cinema.`);
        console.log(`Cinema income - ${income} lv.`);

    }


}


cinema(["100",
"15",
"15",
"15",
"15",
"15",
"15",
"15"])