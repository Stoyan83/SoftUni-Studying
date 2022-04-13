function numbers(input) {
    let firstPlayer = input[0];
    let secondPlayer = input[1];
    let pointsFirstPlayer = 0;
    let pointsSecondPlayer = 0;

    for (let i = 2; i < input.length; i += 2) {
        let card = input[i]
        if (card === "End of game") {
            console.log(`${firstPlayer} has ${pointsFirstPlayer} points`);
            console.log(`${secondPlayer} has ${pointsSecondPlayer} points`);
            break;
        } else {
            let first = Number(input[i]);
            let second = Number(input[i + 1]);
            if (first > second) {
                pointsFirstPlayer += (first - second)
            } else if (first < second) {
                pointsSecondPlayer += second - first;
            } else {
                console.log(`Number wars!`);
                first = Number(input[i += 2]);
                second = Number(input[i + 1]);
                if (first > second) {
                    console.log(`${firstPlayer} is winner with ${pointsFirstPlayer} points`);
                    break;
                } else if (first < second) {
                    console.log(`${secondPlayer} is winner with ${pointsSecondPlayer} points`);
                    break;
                }
            }

        }
    }
}

numbers(["Desi",
"Niki",
"7",
"5",
"3",
"4",
"3",
"3",
"5",
"3"])