function timeNeeded(input) {
    let name = input[0];
    let projectNumber = Number(input[1]);
    let totalHours = projectNumber * 3;
    console.log(`The architect ${name} will need ${totalHours} hours to complete ${projectNumber} project/s.`);
}

timeNeeded(["George ","4 "]);