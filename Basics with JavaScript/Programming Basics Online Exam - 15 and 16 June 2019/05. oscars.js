function oscars(input) {
    let name = input[0];
    let startingPoints = Number(input[1]);
    let numberOfJury = Number(input[2])
    const scoreNeeded = 1250.5;

    let index = 3

    for (let i = 0; i < numberOfJury; i++) {
        if (startingPoints > scoreNeeded) {
            break
        }
        let juryName = String(input[index++])
        let score = Number(input[index++])
        
        startingPoints += juryName.length * score / 2
    }
    if (startingPoints > scoreNeeded) {
        console.log(`Congratulations, ${name} got a nominee for leading role with ${startingPoints.toFixed(1)}!`);
    } else {
        console.log(`Sorry, ${name} you need ${(scoreNeeded - startingPoints).toFixed(1)} more!`);
    }
}


oscars(["Zahari Baharov",
"205",
"4",
"Johnny Depp",
"45",
"Will Smith",
"29",
"Jet Lee",
"10",
"Matthew Mcconaughey",
"39"])