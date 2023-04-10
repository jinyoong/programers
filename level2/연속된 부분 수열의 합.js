function solution(sequence, k) {
  let answer = [];
  let minLength = Infinity;
  let start = 0;
  let sum = 0;

  for (end = 0; end < sequence.length; end++) {
    const current = sequence[end];
    let currentLength = end - start + 1;
    sum += current;

    if (sum === k && currentLength < minLength) {
      answer = [start, end];
      minLength = currentLength;
    } else if (sum > k) {
      while (sum > k) {
        sum -= sequence[start];
        currentLength -= 1;
        start += 1;

        if (sum === k) {
          if (currentLength < minLength) {
            answer = [start, end];
            minLength = currentLength;
          };

          break;
        };

        if (start >= end) {
          break;
        };
      };
    };
  };

  return answer;
};

console.log(solution([1, 2, 3, 4, 5], 7));
console.log(solution([1, 1, 1, 2, 3, 4, 5], 5));
console.log(solution([2, 2, 2, 2, 2], 6))