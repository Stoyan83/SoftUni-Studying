function nameGame(input) {
    let index = 0;
    let name = input[index];
    index++;
    let playerPoints = 0;
    let winnerName = '';
    let winnerPoints = 0;


    while (name !== "Stop") {
        playerPoints = 0
        
        for (ch of name) {
            let char = Number(input[index])
            index++;
            if (ch.charCodeAt(0) === char) {
                playerPoints += 10;
            } else {
                playerPoints += 2;
            }
        }
        if (playerPoints >= winnerPoints) {
            winnerPoints = playerPoints;
            winnerName = name;
        }
        name = input[index++];

    }
    console.log(`The winner is ${winnerName} with ${winnerPoints} points!`);    
}


nameGame(["Ivan",
    "73",
    "20",
    "98",
    "110",
    "Ivo",
    "80",
    "65",
    "87",
    "Stop"]);