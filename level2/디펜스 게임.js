function solution(n, k, enemy) {
  let answer = 0;

  function countFunc(idx, count, result, soliderCount){

    if (result > answer) answer = result;

    if (count > 0) {
      countFunc(idx + 1, count - 1, result + 1, soliderCount);
    };

    if (enemy[idx] <= soliderCount) {
      countFunc(idx + 1, count, result + 1, soliderCount - enemy[idx]);
    };

    if (enemy[idx] > soliderCount) {
      if (answer < result) answer = result;
    };
  };

  countFunc(0, k, 0, n);

  return answer;
};

console.log(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]));