function solution(maps) {
  let answer = [];
  const width = maps[0].length;
  const height = maps.length;
  const visited = new Array(height).fill(0).map(() => new Array(width).fill(0));
  const direction = [[-1, 0], [0, 1], [1, 0], [0, -1]];

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      const current = maps[r][c];

      if (current === 'X') continue;

      if (visited[r][c] === 1) continue;

      let stack = [[r, c]];
      let result = Number(current);
      visited[r][c] = 1;
      
      while (stack.length >= 1) {
        const [sr, sc] = [...stack.pop()];

        for (let d of direction) {
          const nr = sr + d[0];
          const nc = sc + d[1];

          if (nr < 0 || nr >= height || nc < 0 || nc >= width) continue;

          if (visited[nr][nc] === 1) continue;

          if (maps[nr][nc] === 'X') continue;

          result += Number(maps[nr][nc]);
          visited[nr][nc] = 1;
          stack.push([nr, nc]);
        };
      };

      answer.push(result);
    };
  };

  if (answer.length === 0) answer.push(-1);

  return answer.sort((a, b) => a - b);
};

console.log(solution(["X591X","X1X5X","X231X", "1XXX1"]));
console.log(solution(["X111XX", "XXX1X2", "XX3XX9"]))
console.log(solution(['111', '1X1', '11X']))