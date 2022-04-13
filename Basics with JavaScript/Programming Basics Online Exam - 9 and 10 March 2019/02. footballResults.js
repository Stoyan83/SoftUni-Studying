function football(input) {
    let win = 0;
    let lose = 0;
    let draw = 0

    for (let i=0; i < input.length; i++){
        let first = Number(input[i][0]);
        let last = Number(input[i][2]);

        if(first > last) {
            win += 1;
        }else if(first < last) {
            lose += 1;
        }else {
            draw += 1;
        }
    }
    console.log(`Team won ${win} games.`);
    console.log(`Team lost ${lose} games.`);
    console.log(`Drawn games: ${draw}`);
}

football(["0:2",
    "0:1",
    "3:3"]);