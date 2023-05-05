function solution(A, B) {
  let answer = 0;
  let sortedA = A.sort((a, b) => a - b);
  let sortedB = B.sort((a, b) => a - b);
  let bIdx = 0;

  for (let i = 0; i < B.length; i++) {
    const elementA = sortedA[i];
    let elementB = sortedB[bIdx];

    while (elementA >= elementB && bIdx < B.length) {
      bIdx += 1;
      elementB = sortedB[bIdx];
    };

    if (elementA < elementB) {
      answer += 1;
      bIdx += 1;
    };

    if (bIdx === B.length) {
      break;
    };
  };

  return answer;
};

console.log(solution([5, 1, 3, 7], [2, 2, 6, 8]));
console.log(solution([5, 1, 3, 7], [2, 2, 4, 8]));