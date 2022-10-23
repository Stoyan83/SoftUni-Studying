function solve(arr) {
  let sortArr = arr.sort((a,b)=> a.localeCompare(b));
  for (let i = 0; i < arr.length; i++) {
    console.log(`${i + 1}.${sortArr[i]}`);
  }
}

solve(["John", "Bob", "Christina", "Ema"]);
