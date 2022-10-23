function solve(arr) {
  let sortArr = arr.sort((a, b) => a - b).slice(0, 2);
  console.log(sortArr.join(" "));
}

solve([3, 0, 10, 4, 7, 3]);
