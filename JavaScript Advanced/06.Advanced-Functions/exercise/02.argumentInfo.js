function solve() {
  const params = Array.from(arguments);

  const types = {};

  for (const arr of params) {
    let type = typeof arr;
    console.log(`${type}: ${arr}`);

    if (types[type] == undefined) {
      types[type] = 0;
    }
    types[type]++;
  }
  const result = Object.entries(types).sort((a, b) => b[1] - a[1]);

  for (let [type, count] of result) {
    console.log(`${type} = ${count}`);
  }
}

solve("cat", 42, function () {
  console.log("Hello world!");
});
