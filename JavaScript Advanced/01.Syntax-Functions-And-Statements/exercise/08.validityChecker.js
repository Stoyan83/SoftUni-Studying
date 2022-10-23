function solve(x1, y1, x2, y2){
  let result = '';
  
  const test1 = Math.sqrt(x1 ** 2 + y1 ** 2);
  result = test1 % 1 == 0 ? 'valid' : 'invalid';
  console.log(`{${x1}, ${y1}} to {0, 0} is ${result}`)

  const test2 = Math.sqrt(x2 ** 2 + y2 ** 2);
  result = test2 % 1 == 0 ? 'valid' : 'invalid';
  console.log(`{${x2}, ${y2}} to {0, 0} is ${result}`)

  const test3 = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
  result = test3 % 1 == 0 ? 'valid' : 'invalid';
  console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${result}`)
}

solve(2, 1, 1, 1)