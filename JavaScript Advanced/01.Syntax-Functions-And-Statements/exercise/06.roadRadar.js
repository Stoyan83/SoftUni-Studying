function solve(speed, area){
  const speedLimits = {
      'motorway': 130,
      'interstate': 90,
      'city': 50, 
      'residential': 20
  }
  let areaLimit = speedLimits[area];
  let difference = speed - areaLimit
  let status = ''
  if (speed <= areaLimit){
      console.log(`Driving ${speed} km/h in a ${areaLimit} zone`);
      return;
  } else if (difference <= 20) {
      status = 'speeding';
  } else if (difference <= 40) {
      status = 'excessive speeding'
  } else {
      status = 'reckless driving'
  }
  console.log(`The speed is ${difference} km/h faster than the allowed speed of ${areaLimit} - ${status}`)
}

solve(200, 'motorway')