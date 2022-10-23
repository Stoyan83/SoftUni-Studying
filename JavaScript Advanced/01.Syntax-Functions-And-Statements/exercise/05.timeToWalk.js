function solve(steps, lenghtOfFootprint, speedKmH) {
  let distanceMeters = steps * lenghtOfFootprint;
  let speed = (speedKmH * 1000) / 3600;
  let breaks = Math.floor(distanceMeters / 500) * 60;
  let timeSeconds = distanceMeters / speed + breaks;

  let hours = Math.floor(timeSeconds / 3600);
  let minutes = Math.floor(timeSeconds / 60);
  let seconds = timeSeconds % 60;

  console.log(
    `${hours.toFixed(0).padStart(2, "0")}:${minutes
      .toFixed(0)
      .padStart(2, "0")}:${seconds.toFixed(0).padStart(2, "0")}`
  );
}

solve(2564, 0.7, 5.5);
