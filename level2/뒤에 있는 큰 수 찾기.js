function solution(numbers) {
  const answer = new Array(numbers.length).fill(-1);
  const stack = [];

  numbers.forEach((element, index) => {
    while (stack.length >= 1 && numbers[stack[stack.length - 1]] < element) {
      answer[stack.pop()] = element;
    }
    stack.push(index);
  });

  while (stack.length >= 1) {
    answer[stack.pop()] = -1;
  }


  return answer;
}

console.log(solution([1]));
console.log(solution([2, 1, 2, 3, 4]));
console.log(solution([9, 1, 5, 3, 6, 2]));