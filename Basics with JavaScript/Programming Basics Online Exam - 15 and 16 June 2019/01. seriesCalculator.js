function seriesCalculator(input) {
    let name = input[0];
    let seasonsNumber = Number(input[1]);
    let episodesNumber = Number(input[2]);
    let duration = Number(input[3]);

    let totalTime = seasonsNumber * episodesNumber *(duration * 1.2) + (seasonsNumber * 10);

    console.log(`Total time needed to watch the ${name} series is ${totalTime} minutes.`);

}


seriesCalculator(["Lucifer",
"3",
"18",
"55"]);