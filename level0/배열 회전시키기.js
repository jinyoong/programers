function solution(numbers, direction) {
  const answer = [...numbers];
  const changeIndex = direction === "left" ? numbers.length - 1 : 1;

  for (let i = 0; i < numbers.length; i++) {
    answer[(i + changeIndex) % numbers.length] = numbers[i]
  }

  return answer;
}