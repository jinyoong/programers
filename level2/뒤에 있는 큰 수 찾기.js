function solution(numbers) {
  const answer = new Array(numbers.length).fill(-1);
  const pair = [numbers[numbers.length - 1], numbers[numbers.length - 1]]

  for (let i = numbers.length - 1; i >= 0; i--) {
    const nextNumber = pair[0];
    const big = pair[1];
    const current = numbers[i];

    pair[0] = current;

    if (current < nextNumber) {
      answer[i] = nextNumber;
    }
    else if (current < big) {
      for (let j = i + 1; j < numbers.length; j++) {
        if (numbers[j] > current) {
          answer[i] = numbers[j];
          break;
        };
      };
    }
    else {
      answer[i] = -1;
      pair[1] = current;
    }
  }

  return answer;
}

console.log(solution([2, 1, 2, 3, 4]));
console.log(solution([9, 1, 5, 3, 6, 2]));