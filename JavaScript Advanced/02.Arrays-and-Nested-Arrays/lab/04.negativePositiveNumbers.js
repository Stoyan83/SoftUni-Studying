function solve(arr) {
  let newArr = [];
  for (const num of arr) {
    if (num < 0) {
      newArr.unshift(num);
    } else {
      newArr.push(num);
    }
  }
  console.log(newArr);
}

solve([7, -2, 8, 9]);
