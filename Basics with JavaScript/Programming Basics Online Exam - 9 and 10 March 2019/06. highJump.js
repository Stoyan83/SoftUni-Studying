function jump(input) {
    let targetHeight = Number(input[0]);
    let startHeight = targetHeight - 30;

    let jump = 0;
    let failAttempts = 0;
    for (let i = 1; i < input.length; i++) {
        let currentHeight = Number(input[i]);
        jump++
        if (currentHeight > startHeight) {
            if (startHeight >= targetHeight) {
                console.log(`Tihomir succeeded, he jumped over ${startHeight}cm after ${jump} jumps.`)
                break;
            }
            startHeight += 5
            failAttempts = 0
        } else {
            failAttempts++
        }


        if (failAttempts == 3) {
            console.log(`Tihomir failed at ${startHeight}cm after ${jump} jumps.`)
        }
    }
}

jump(["250",
"225",
"224",
"225",
"228",
"231",
"235",
"234",
"235"])