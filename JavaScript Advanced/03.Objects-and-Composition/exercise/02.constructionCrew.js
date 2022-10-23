function solve(arr) {
  if (arr.dizziness == true) {
    arr.levelOfHydrated += Number((arr.weight * arr.experience) * 0.1)
    arr.dizziness = false
  }
  
  return arr
}


solve({ weight: 80,
  experience: 1,
  levelOfHydrated: 0,
  dizziness: true })

solve({ weight: 120,
  experience: 20,
  levelOfHydrated: 200,
  dizziness: true })

solve({ weight: 95,
  experience: 3,
  levelOfHydrated: 0,
  dizziness: false })