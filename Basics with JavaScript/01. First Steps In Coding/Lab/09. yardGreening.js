function yardGreening(input) {
    const priceSquareMeter = 7.61;    
    let metersForGreening = input[0]
    let totalPrice = metersForGreening * priceSquareMeter 
    let discount = totalPrice * 0.18
    let priceWithDiscount = totalPrice - discount
    console.log(`The final price is: ${priceWithDiscount} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}

yardGreening(["550"])