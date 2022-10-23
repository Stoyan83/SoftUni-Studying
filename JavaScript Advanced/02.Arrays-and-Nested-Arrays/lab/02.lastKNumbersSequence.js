function solve(num1, num2){let array = [1]
for (let i = 1; i < num1; i++) {
    let arg = array.slice(Math.max(0, i - num2), i).reduce((a, b) => a + b);
    array.push(arg);
}
return array;
}

console.log(solve(6, 3));