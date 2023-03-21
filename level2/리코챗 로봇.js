function solution(board) {
  let answer = -1;
  const direction = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  let visited = new Array(board.length).fill(0).map(() =>  new Array(board[0].length).fill(0));
  let queue = [];
  let idx = 0;

  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      const element = board[r][c];

      if (element === "R") {
        queue.push([r, c, 0]);
        visited[r][c] = 1;
        break;
      };
    };
  };

  while (idx < queue.length) {
    const r = queue[idx][0];
    const c = queue[idx][1];
    const count = queue[idx][2];
    idx += 1;

    if (board[r][c] === "G") {
      answer = count;
      break;
    };

    for (let d of direction) {
      let nr = r + d[0];
      let nc = c + d[1];

      while (!isStop(nr, nc, board)) {
        nr += d[0];
        nc += d[1];
      };

      nr -= d[0];
      nc -= d[1];

      if (visited[nr][nc] === 1) {
        continue;
      };

      visited[nr][nc] = 1;
      queue.push([nr, nc, count + 1]);
    };
  };

  return answer;
};

function isStop(r, c, board) {
  if (r < 0 || r >= board.length || c < 0 || c >= board[0].length) {
    return true;
  };

  if (board[r][c] === "D") {
    return true;
  };

  return false;
};

console.log(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]));