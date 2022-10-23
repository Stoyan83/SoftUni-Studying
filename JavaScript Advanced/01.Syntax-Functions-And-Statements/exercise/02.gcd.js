function solve(a, b) {
  if (a == 0) return b;
  return solve(b % a, a);
}

console.log(solve(2154, 458));
