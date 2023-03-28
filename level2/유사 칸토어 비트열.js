function solution(n, l, r) {
  let answer = 0;

  answer = req(l - 1, r - 1, n - 1);

  return answer;
};

function req(left, right, k) {
  let result = 0;

  if (k === 0) {
    for (let i = left; i <= right; i++) {
      if (i === 2) {
        continue;
      };

      result += 1;
    };

    return result;
  };

  for (let i = 0; i < 5; i++) {
    if (i === 2) {
      continue;
    };

    const start = 5 ** k * i;
    const end = 5 ** k * (i + 1) - 1;
    
    if (end < left) {
      continue;
    } else if (start > right) {
      continue;
    } else if (start >= left && end <= right) {
      result += 4 ** k;
    } else if (start >= left && end > right) {
      const newLeft = 0;
      const newRight = right - start;

      result += req(newLeft, newRight, k - 1);
    } else if (start < left && end <= right) {
      const newLeft = left - start;
      const newRight = end % (5 ** k);

      result += req(newLeft, newRight, k - 1);
    } else if (start < left && end > right) {
      const newLeft = left - start;
      const newRight = right - start;

      result += req(newLeft, newRight, k - 1);
    };
  };

  return result;
};

/*
0: 1, 1개
1: A, 5개, 2
2: AABAA, 25개, 1번째 위치 + 5 * (0, 1, 3, 4) + 5 ^ (n - 1) * 2 ~ (5 ^ (n - 1)) - 1 
3: CCDCC, 125개, 2번째 위치 + 5 * (0, 1, 3, 4) + 5 ^ (n - 1) * 2 ~ (5 ^ (n - 1)) - 1 
4: EEFEE

*/

console.log(solution(2, 4, 17));
console.log(solution(1, 2, 4));
console.log(solution(3, 70, 125));
console.log(solution(4, 30, 118));
console.log(solution(3, 1, 125));
console.log(solution(4, 27, 68));
console.log(solution(20, 1, 5 ** 20));
console.log(solution(20, 5 ** 10, 5 ** 20));