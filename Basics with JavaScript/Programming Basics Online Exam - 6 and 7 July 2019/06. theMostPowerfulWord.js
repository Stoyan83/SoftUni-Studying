function wordPower(input) {
    let sum = 0
    let powerWord = ''
    let current_sum = 0;
    for (let i = 0; i < input.length - 1; i++) {
        word = input[i];
        sum = 0
        for (let j = 0; j < word.length; j++) {
            sum += word.charCodeAt(j)

        } if (word[0] == "E" || word[0] == "A" || word[0] == "I" || word[0] == "O"|| word[0] == "U"||word[0] == "Y"||
        word[0] == "e" || word[0] == "a" || word[0] == "i" || word[0] == "o"|| word[0] == "u"||word[0] == "y") {
            sum *= word.length
        } else {
            sum = Math.floor(sum/word.length)
        }
        if (sum > current_sum) {
            current_sum = sum
            powerWord = word
        }

    }
console.log(`The most powerful word is ${powerWord} - ${current_sum}`);
}

wordPower(["But",
"Some",
"People",
"Say",
"It's",
"LOVE",
"End of words"])