function solve(arr) {
  let newArr = [];

  for (let i = 1; i < arr.length; i += 2) {
    newArr.push(arr[i] * 2);
  }
  return newArr.reverse().join(" ");
}

console.log(solve([10, 15, 20, 25]));
