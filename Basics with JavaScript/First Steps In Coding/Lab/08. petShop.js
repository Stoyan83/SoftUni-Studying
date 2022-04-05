function petShop(input) {
    const dogFood = 2.5;
    const catFood = 4;
    let quantityDogFood = input[0];
    let quantityCatFood = input[1];
    let totalPrice = (dogFood * quantityDogFood + catFood * quantityCatFood);
    console.log(`${totalPrice} lv.`);
}

petShop(["5 ",
"4 "])