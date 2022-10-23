function solve(arr) {
  const sortArr = arr.sort((a, b) => a.length - b.length || a.localeCompare(b));
  console.log(sortArr.join("\n"));
}

solve(["alpha", "beta", "gamma"]);
