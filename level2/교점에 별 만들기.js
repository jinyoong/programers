function solution(line) {
  let answer = [];
  let dots = [];
  let left = Infinity;
  let right = -Infinity;
  let top = -Infinity;
  let bottom = Infinity;
  let isInDot = false;

  for (let i = 0; i < line.length - 1; i++) {
    const A = line[i][0];
    const B = line[i][1];
    const E = line[i][2];

    for (let j = i + 1; j < line.length; j++) {
      const C = line[j][0];
      const D = line[j][1];
      const F = line[j][2];
      const parallel = A * D - B * C;

      if (parallel === 0) {
        continue;
      };

      if ((B * F - E * D) % parallel !== 0) {
        continue;
      };

      if ((E * C - A * F) % parallel !== 0) {
        continue;
      };

      isInDot = true;
      const x = (B * F - E * D) / parallel;
      const y = (E * C - A * F) / parallel;

      if (x < left) {
        left = x;
      };
      
      if (x > right) {
        right = x;
      };
      
      if (y < bottom) {
        bottom = y;
      };
      
      if (y > top) {
        top = y;
      };

      dots.push([x, y]);
    };
  };

  if (!isInDot) {
    return answer;
  };

  let board = new Array(top - bottom + 1).fill(0).map(() => new Array(right - left + 1).fill('.'));
  dots.forEach(element => {
    const r = top - element[1];
    const c = element[0] - left;

    board[r][c] = "*";
  });

  board.forEach(element => {
    answer.push(element.join(""));
  });

  return answer;
};

console.log(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]));
console.log(solution([[-1, 1, 0], [-2, 1, 0], [0, 1, -2]]));