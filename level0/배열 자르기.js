function solution(numbers, num1, num2) {
  const answer = numbers.filter((element, index) => (index >= num1 && index <= num2))
  const answer2 = numbers.splice(num1, num2 + 1)
  console.log(answer2)
  return answer;
}