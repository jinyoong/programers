function solution(numbers) {
  var answer = [];

  numbers.map(number => {
    answer.push(number * 2)
  })

  return answer;
}