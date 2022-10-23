function solve(arr) {
  let newArr = [];
  let maxNum = Number.MIN_SAFE_INTEGER;
  for (const num of arr) {
    if (num >= maxNum) {
      maxNum = num;
      newArr.push(maxNum);
    }
  }
  return newArr
}

console.log(solve([1, 3, 8, 4, 10, 12, 3, 2, 24]));
