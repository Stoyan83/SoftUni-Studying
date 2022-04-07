function food(input) {
    let chicken = 10.35;
    let fish = 12.4;
    let vegetarian = 8.15;
    let numberOfChicken = Number(input[0]);
    let numberOfFish = Number(input[1]);
    let numberOfVegetarian = Number(input[2]);
    let total = chicken * numberOfChicken + fish * numberOfFish + vegetarian * numberOfVegetarian;
    let desert = total * 0.2;
    let totalSum = total + desert + 2.5;
    console.log(totalSum);
}

food(["2 ",
"4 ",
"3 "]);