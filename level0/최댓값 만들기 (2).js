function solution(numbers) {
  const n = numbers.length
  numbers.sort((a, b) => a - b);

  return Math.max(numbers[0] * numbers[1], numbers[n - 2] * numbers[n - 1]);
}