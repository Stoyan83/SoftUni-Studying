function tennis(input) {
    let numberOfTournaments = input[0];
    let startingPoints = Number(input[1]);
    let totalPoints = 0;
    let w = 0;

    for (let i=2; i <= numberOfTournaments + 1; i++){
        let place = input[i]
        if(place === "W"){
            totalPoints += 2000;
            w += 1
        }else if (place === "F"){
            totalPoints += 1200;
        }else if (place === "SF"){
            totalPoints += 720;
        }
    }
    console.log(`Final points: ${totalPoints + startingPoints}`);
    console.log(`Average points: ${Math.floor(totalPoints/numberOfTournaments)}`);
    console.log(`${((w/numberOfTournaments)*100).toFixed(2)}%`);
}

tennis(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"]);
