function tennis(input) {
    let priceTennisRacket = Number(input[0]);
    let countTennisRackets = Number(input[1]);
    let countSneakers = Number(input[2]);

    let priceSneakers = priceTennisRacket / 6
    let total = priceSneakers * countSneakers + countTennisRackets * priceTennisRacket
    let otherEquipment = total * 0.2
    let totalSum = total + otherEquipment

    
    console.log(`Price to be paid by Djokovic ${Math.floor(totalSum/8)}`);
    console.log(`Price to be paid by sponsors ${Math.ceil((totalSum/8) * 7)}`);
}

tennis(["850" , "4" , "2"]);