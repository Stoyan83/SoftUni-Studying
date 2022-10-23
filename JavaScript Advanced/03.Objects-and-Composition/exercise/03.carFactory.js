function solve(arr) {
  const engines = [
    { power: 90, volume: 1800 },
    { power: 120, volume: 2400 },
    { power: 200, volume: 3500 },
  ];
  const carriages = [
    { type: "hatchback", color: arr.color },
    { type: "coupe", color: arr.color },
  ];
  const wheels = (wheelSize) =>
    Array(4).fill(wheelSize % 2 == 1 ? wheelSize : wheelSize - 1);

  return {
    model: arr.model,
    engine: engines.filter((e) => e.power >= arr.power)[0],
    carriage: carriages.filter((c) => c.type == arr.carriage)[0],
    wheels: wheels(arr.wheelsize),
  };
}

console.log(
  solve({
    model: "VW Golf II",
    power: 90,
    color: "blue",
    carriage: "hatchback",
    wheelsize: 14,
  })
);

solve({
  model: "Opel Vectra",
  power: 110,
  color: "grey",
  carriage: "coupe",
  wheelsize: 17,
});
