function solve(arr, el) {
  let newArr = [];
  for (let i = 0; i < arr.length; i += el) {
    newArr.push(arr[i]);
  }
  return newArr;
}

console.log(solve(["5", "20", "31", "4", "20"], 2));
