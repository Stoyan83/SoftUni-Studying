function favoriteMovie(input) {
    let index = 0;
    let command = input[index++];
    let bestScore = 0;
    let bestMovie = "";
    let count = 0;

    while (command !== "STOP") {
        count += 1
        if (count === 7) {
            break
        }
        word = String(command)
        let currentScore = 0
        let len = word.length
        for (let i = 0; i < word.length; i++) {

            if ("A" <= word[i] && word[i] <= "Z") {
                
                currentScore += word[i].charCodeAt(0) - word.length

            } else if ("a" <= word[i] && word[i] <= "z") {
                
                
                currentScore += word[i].charCodeAt(0) - (word.length * 2);


            } else {
                currentScore += word[i].charCodeAt(0)
            }

            if (currentScore > bestScore) {
                bestScore = currentScore
                bestMovie = word

            }
            ;
        }
        command = input[index++];
    }
    if (count >= 7){
        console.log(`The limit is reached.
        The best movie for you is ${bestMovie} with ${bestScore} ASCII sum.`);
    } else {
        console.log(`The best movie for you is ${bestMovie} with ${bestScore} ASCII sum.`);
    }
    
}

favoriteMovie(["Wrong turn",
"The maze",
"Area 51",
"Night Club",
"Ice age",
"Harry Potter",
"Wizards"])