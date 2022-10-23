function solve(params) {
  console.log(params.toUpperCase()
  .match(/\w+/g)
  .join(", "));
}

solve('Hi, how are you?');
