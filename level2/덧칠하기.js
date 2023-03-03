function solution(n, m, section) {
  let answer = 0;
  let isVisited = new Set();
  let idx = 0;

  while (idx < section.length) {
    const currentElement = section[idx];

    if (isVisited.has(currentElement)) {
      idx += 1;
      continue;
    };

    for (let nextIdx = idx; nextIdx < section.length; nextIdx++) {
      const nextElement = section[nextIdx];
      
      if (nextElement >= currentElement + m) break;

      isVisited.add(nextElement);
      idx = nextIdx;
    };

    answer += 1;
  };

  return answer;
};

console.log(solution(8, 4, [2, 3, 6]));
console.log(solution(5, 2, [1, 5]));