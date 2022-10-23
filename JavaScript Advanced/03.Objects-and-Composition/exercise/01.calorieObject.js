function solve(array) {
  obj = {};

  for (let index = 0; index < array.length; index += 2) {
    const keyArr = array[index];
    const valueArr = Number(array[index + 1]);
    obj[keyArr] = valueArr;
  }

  console.log(obj);
}

solve(["Yoghurt", "48", "Rise", "138", "Apple", "52"]);
solve(["Potato", "93", "Skyr", "63", "Cucumber", "18", "Milk", "42"]);
