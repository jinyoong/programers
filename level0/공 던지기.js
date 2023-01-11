function solution(numbers, k) {
  var answer = 1;
  const len = numbers.length
  let idx = 0;
  let count = 1;

  while (count !== k) {
    idx = (idx + 2) % len
    answer = numbers[idx];
    count += 1
  }

  return answer;
}