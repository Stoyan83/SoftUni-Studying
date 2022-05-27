function movieStars(input) {

    let budget = Number(input[0])
    let index = 1
    let command = input[index++]
    let currentBudget = budget


    while (command !== "ACTION") {

        let actorName = String(command)
        if (currentBudget < 0) {

            break
        }
        if (actorName.length <= 15) {
            let money = Number(input[index++])
            currentBudget -= money
        } else {
            currentBudget -= currentBudget * 0.2

        }
        command = input[index++]
    }

    if (currentBudget >= 0) {
        console.log(`We are left with ${currentBudget.toFixed(2)} leva.`);
    } else {
        console.log(`We need ${Math.abs(currentBudget).toFixed(2)} leva for our actors.`);
    }
}

movieStars(["1000",
    "John Cena",
    "800",
    "Freddy Kim",
    "3000",
    "ACTION"])