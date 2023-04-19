function solution(r1, r2) {
  let answer = 0;

  answer = countOnAxis(r1, r2) + countInQuadrant(r1, r2);

  return answer;
};

function countOnAxis(r1, r2) {
  return (r2 - r1 + 1) * 4;
};

function countInQuadrant(r1, r2) {
  let result = 0;
  
  for (let x = 1; x < r2; x++) {
    const minimum = Math.ceil(Math.sqrt(r1 ** 2 - x ** 2) || 0);
    const maximum = parseInt(Math.sqrt(r2 ** 2 - x ** 2));

    if (minimum === 0) {
      result += maximum - minimum;
    } else {
      result += maximum - minimum + 1;
    };
  };

  return result * 4;
};

console.log(solution(2, 3));
console.log(solution(2, 4));