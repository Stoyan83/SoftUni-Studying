function add(n) {
  const inner = function (num) {
    n += num
    return inner
  }
inner.toString = function () {
  return n
}

  return inner
}


console.log(add(1).toString())
console.log(add(1)(6)(-3).toString())