function timeForReading(input) {
    let bookPages = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let days = Number(input[2]);
    let hoursPerDay = (bookPages / days) / pagesPerHour;
    console.log(hoursPerDay);
}

timeForReading(["212 ",
"20 ",
"2 "]
);