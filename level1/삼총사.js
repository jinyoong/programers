function solution(number) {
  var answer = 0;

  function sumOfNumber(result, idx, count) {

    if (count === 3) {
      if (result === 0) {
        console.log(numberArray)
        answer += 1
      }
      return
    }

    for (let i = idx; i < number.length; i++) {
      sumOfNumber(result + number[i], i + 1, count + 1)
    }

  }

  sumOfNumber(0, 0, 0)

  return answer;
}


console.log(solution([-2, 3, 0, 2, -5]))
console.log(solution([-3, -2, -1, 0, 1, 2, 3]))
console.log(solution([-1, 1, -1, 1]))