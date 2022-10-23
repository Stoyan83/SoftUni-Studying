function solve(number, ...arr) {
  const actions = {
    chop: (x) => x / 2,
    dice: (x) => Math.sqrt(x),
    spice: (x) => x + 1,
    bake: (x) => x * 3,
    fillet: (x) => x - x * 0.2,
  };

  let num = Number(number);
  for (const action of arr) {
    num = actions[action](num);
    console.log(num);
  }
}

solve("9", "dice", "spice", "chop", "bake", "fillet");
