function solve(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
      process.stdout.write(arr[i] + " ");
    }
  }
}

solve(["20", "30", "40", "50", "60"]);
