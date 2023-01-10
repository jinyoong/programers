function solution(emergency) {
  const sortedEmergency = [...emergency].sort((a, b) => b - a)
  return emergency.map(element => sortedEmergency.indexOf(element) + 1);
}

console.log(solution([3, 1, 7]))
console.log(solution([3, 76, 24]))