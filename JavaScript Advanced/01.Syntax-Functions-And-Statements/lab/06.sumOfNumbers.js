function solve(x, y) {
  let num1 = Number(x);
  let num2 = Number(y);
  let result = 0;

  for (let index = num1; index <= num2; index++) {
    result += index;
  }
  return result
}

solve("-8", "20");
