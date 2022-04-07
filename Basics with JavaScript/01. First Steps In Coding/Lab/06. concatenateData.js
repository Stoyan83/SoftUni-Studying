function concatenate(data) {
    let firstName = data[0];
    let lastName = data[1];
    let age =  data[2];
    let town = data[3];
    console.log(`You are ${firstName} ${lastName}, a ${age}-years old person from ${town}.`);
}


concatenate(['Maria', 'Ivanova', 20, 'Sofia']);