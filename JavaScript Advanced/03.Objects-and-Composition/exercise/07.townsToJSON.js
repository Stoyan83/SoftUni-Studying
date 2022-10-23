function solve(arr) {
  let result = [];

  class Town {
    constructor(town, lattitude, longitude) {
      this.Town = town;
      this.Latitude = Number(lattitude);
      this.Longitude = Number(longitude);
    } 
  }

  for (let i = 1; i < arr.length; i++) {
    let current = arr[i]
      .split("|")
      .map((t) => t.trim())
      .filter((x) => x.length != 0);
    let townName = current[0];
    let lattitude = Number(current[1]).toFixed(2);
    let longitude = Number(current[2]).toFixed(2);
    let town = new Town(townName, lattitude, longitude);
    result.push(town);
  }

  console.log(JSON.stringify(result));
}

solve([
  "| Town | Latitude | Longitude |",
  "| Sofia | 42.696552 | 23.32601 |",
  "| Beijing | 39.913818 | 116.363625 |",
]);
