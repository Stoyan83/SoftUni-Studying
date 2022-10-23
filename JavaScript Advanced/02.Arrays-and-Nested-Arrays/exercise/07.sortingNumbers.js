function solve(arr) {
  const finalArr = [];
  const newArr = arr.sort((a, b) => a - b);
  while (newArr.length) {
    finalArr.push(newArr.shift(), newArr.pop());
  }
  return finalArr;
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
