function solve(arr) {
  let sortArr = arr.sort((a, b) => a - b);
  return sortArr.slice(Math.ceil((arr.length - 1) / 2), arr.length);
}

console.log(solve([3, 19, 14, 7, 2, 19, 6]));
