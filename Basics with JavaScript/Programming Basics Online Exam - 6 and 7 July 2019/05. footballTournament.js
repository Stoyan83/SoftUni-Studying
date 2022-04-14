function football(input) {
    let teamName = input[0];
    let playedGames = Number(input[1]);
    let win = 0;
    let lose = 0;
    let draw = 0;

    for (let i = 2; i <= playedGames + 1; i++) {
        let result = input[i];
        if (result === "W") {
            win += 1;
        } else if (result === "L") {
            lose += 1;
        } else {
            draw += 1;
        }
    }
    let score = win * 3 + draw * 1;
    if (playedGames > 0) {
        console.log(`${teamName} has won ${score} points during this season.`);
        console.log(`Total stats:`);
        console.log(`## W: ${win}`);
        console.log(`## D: ${draw}`);
        console.log(`## L: ${lose}`);
        console.log(`Win rate: ${(win / playedGames * 100).toFixed(2)}%`);
    }else {
        console.log(`${teamName} hasn't played any games during this season.`);
    }
}

football(["Barcelona",
"7",
"W",
"D",
"L",
"L",
"W",
"W",
"D"])