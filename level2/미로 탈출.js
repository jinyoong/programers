function bfs(start, end, maps, width, height) {
  let result = -1;
  let idx = 0;
  const queue = [[...start, 0]];
  const visited = new Set(start.join(':'));

  while (idx < queue.length) {
    const sr = queue[idx][0];
    const sc = queue[idx][1];
    const count = queue[idx][2];
    idx += 1;

    if (sr === end[0] && sc === end[1]) {
      result = count;
      break;
    };

    for (let d of [[-1, 0], [0, 1], [1, 0], [0, -1]]) {
      const nr = sr + d[0];
      const nc = sc + d[1];

      if (nr < 0 || nr >= height || nc < 0 || nc >= width) {
        continue;
      };

      if (visited.has(`${nr}:${nc}`)) {
        continue;
      };

      if (maps[nr][nc] === 'X') {
        continue;
      };

      queue.push([nr, nc, count + 1]);
      visited.add(`${nr}:${nc}`);
    };
  };

  return result;
};


function solution(maps) {
  let answer = 0;
  const width = maps[0].length;
  const height = maps.length;

  let startPoint = [];
  let leverPoint = [];
  let endPoint = [];
  let LToECount = -1;
  let SToLCount = -1;

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      if (maps[r][c] === 'S') {
        startPoint = [r, c];
      };

      if (maps[r][c] === 'L') {
        leverPoint = [r, c];
      };

      if (maps[r][c] === 'E') {
        endPoint = [r, c];
      };
    };
  };

  SToLCount = bfs(startPoint, leverPoint, maps, width, height);
  LToECount = bfs(leverPoint, endPoint, maps, width, height);

  if (LToECount === -1) return -1;

  if (SToLCount === -1) return -1;

  answer = SToLCount + LToECount;

  return answer;
};

console.log(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]));
console.log(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]));