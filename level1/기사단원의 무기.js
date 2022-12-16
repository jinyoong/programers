function solution(number, limit, power) {
  var answer = 0;
  
  for (let i = 1; i <= number; i++) {
    const tempNumber = countNumber(i);
    answer += tempNumber > limit ? power : tempNumber;
  }

  return answer;
}

function countNumber(number) {
  let result = 0;

  for (let i = 1; i <= Math.sqrt(number); i++) {
    
    if (number % i === 0) {
      result += 2
    }

    if (i * i == number) {
      result -= 1
    }

  }

  return result;
}

console.log(solution(5, 3, 2));
console.log(solution(10, 3, 2));