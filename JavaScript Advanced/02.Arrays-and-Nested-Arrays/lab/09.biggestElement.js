function solve(arr) {
  let newArr = [];
  for (let row = 0; row < arr.length; row++) {
    for (let col = 0; col < arr[row].length; col++) {
      newArr.push(Number(arr[row][col]));
    }
  }
  console.log(Math.max(...newArr));
}

console.log();
solve([
  [20, 50, 10],
  [8, 33, 145],
]);
