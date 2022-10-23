function solve(matrix) {
  let first = 0;
  second = 0;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix.length; j++) {
      if (i == j) first += matrix[i][j];

      if (i + j == matrix.length - 1) second += matrix[i][j];
    }
  }
  console.log(first, second);
}

solve([
  [3, 5, 17],
  [-1, 7, 14],
  [1, -8, 89],
]);
