function solution(k, tangerine) {
  var answer = 0;

  const numbers = new Object();

  tangerine.map((element) => {
    if (element in numbers) {
      numbers[element] += 1
    } else {
      numbers[element] = 1
    }
  })

  const numberArray = Object.values(numbers).sort((a, b) => b - a)
  let idx = 0;

  while (k > 0) {
    k -= numberArray[idx];
    idx += 1
    answer += 1
  }

  return answer;
}

console.log(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]));
console.log(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]));
console.log(solution(2,	[1, 1, 1, 1, 2, 2, 2, 3]));