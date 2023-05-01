function solution(n, works) {
  let answer = 0;
  const total = works.reduce((acc, cur) => acc + cur, 0);

  if (total <= n) {
    return answer;
  };

  const sortedWorks = works.sort((a, b) => b - a);

  let before = sortedWorks[0];
  let beforeCount = 1;
  let remain = n;
  
  for (let i = 1; i < works.length; i++) {
    const current = sortedWorks[i];

    if (current !== before) {
      const needN = before - current;

      if (needN * beforeCount <= remain) {
        remain -= needN * beforeCount;
        before = current;
      } else {
        break;
      };
    };

    beforeCount += 1;
  };

  const possible = parseInt(remain / beforeCount);
  const possibleRemain = remain % beforeCount;

  for (let i = 0; i < beforeCount; i++) {
    if (i < possibleRemain) {
      answer += (before - possible - 1) ** 2;
    } else {
      answer += (before - possible) ** 2;
    };
  };

  for (let i = beforeCount; i < works.length; i++) {
    answer += works[i] ** 2;
  };

  return answer;
};

console.log(solution(4, [4, 3, 3]));
console.log(solution(1, [2, 1, 2]));
console.log(solution(3, [2, 2, 2]));
console.log(solution(999, [800, 100, 55, 45]));
console.log(solution(99, [2, 15, 22, 55, 55])); // 580

// 22 22 22 15 2 - 66
// 15 15 15 15 2 - 87