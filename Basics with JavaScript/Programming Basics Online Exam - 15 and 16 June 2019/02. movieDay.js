function movieDay(input) {
    let ShootingTime = Number(input[0]);
    let numberScenes = Number(input[1]);
    let sceneTime = Number(input[2]);

    let scenePrepare = ShootingTime * 0.15;
    let totalTimeNeeded = scenePrepare + numberScenes * sceneTime;

    if (ShootingTime >= totalTimeNeeded  ) {
        console.log(`You managed to finish the movie on time! You have ${Math.round(Math.abs(ShootingTime - totalTimeNeeded))} minutes left!`);
       
    } else {
        console.log(`Time is up! To complete the movie you need ${Math.round(Math.abs(ShootingTime - totalTimeNeeded))} minutes.`);
    }
    
}


movieDay(["60",
"15",
"3"])