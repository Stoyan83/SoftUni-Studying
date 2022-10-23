function solve(arr) {
  newArr = [];
  result = 0;
  for (let i = 0; i < arr.length; i++) {
    result++;
    if (arr[i] === "add") {
      newArr.push(result);
    } else {
      newArr.pop();
    }
  }
  if (!newArr.length) {
    console.log(`Empty`);
  } else {
    console.log(newArr.join("\n"));
  }
}

solve(["add", "add", "add", "add"]);

solve(["remove", "remove", "remove"]);
