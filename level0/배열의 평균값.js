function solution(numbers) {
  var answer = 0;

  answer = numbers.reduce((prev, curr) => prev + curr)
  answer /= numbers.length

  return answer;
}