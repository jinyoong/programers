function solution(n, m, section) {
  let answer = 0;
  let idx = 0;

  while (idx < section.length) {
    const currentElement = section[idx];
    const startIdx = idx;

    for (let nextIdx = startIdx; nextIdx < section.length; nextIdx++) {
      const nextElement = section[nextIdx];
      
      if (nextElement >= currentElement + m) break;

      idx = nextIdx + 1;
    };

    answer += 1;
  };

  return answer;
};

console.log(solution(8, 4, [2, 3, 6]));
console.log(solution(5, 2, [1, 5]));