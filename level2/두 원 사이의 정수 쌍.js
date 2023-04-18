function solution(r1, r2) {
  let answer = 0;

  answer = countOnAxis(r1, r2) + countOnQuadrant(r1, r2);

  return answer;
};

function countOnAxis(r1, r2) {
  return (r2 - r1 + 1) * 4;
};

function countOnQuadrant(r1, r2) {
  let result = 0;
  
  for (let x = 1; x < r2; x++) {
    const minimum = Math.ceil(Math.sqrt(Math.max(0, r1 ** 2 - x ** 2)));
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

/*
(x + y) ** 2 - 2xy >= r1 ** 2
(x + y) ** 2 - 2xy <= r2 ** 2

2xy <= (x + y) ** 2 - r1 ** 2 = (x + y + r1)(x + y - r1)
2xy >= (x + y) ** 2 - r2 ** 2 = (x + y + r2)(x + y - r2)

(x + y) ** 2 >= r1 ** 2 + 2xy
(x + y) ** 2 <= r2 ** 2 + 2xy

1. 축 위에 있는 경우
x ** 2 >= r1 ** 2
x ** 2 <= r2 ** 2 => r1 <= x <= r2
or
y ** 2 >= r1 ** 2
y ** 2 <= r2 ** 2 => r1 <= y <= r2

2. y = x 위에 있는 경우
4x ** 2 >= r1 ** 2 + 2x ** 2
4x ** 2 <= r2 ** 2 + 2x ** 2
2x ** 2 >= r1 ** 2
2x ** 2 <= r2 ** 2

y = -x + k
x + y = k (x >= 1, y >= 1)
(r1 + 1) ** 2 >= r1 ** 2 + 2xy
2r1 + 1 >= 2xy
*/