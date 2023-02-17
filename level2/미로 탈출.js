function solution(maps) {
  let answer = 0;
  const width = maps[0].length;
  const height = maps.length;
  const direction = [[-1, 0], [0, 1], [1, 0], [0, -1]];

  let LToECount = -1;
  let SToLCount = -1;
  const LToE = [];
  const visited = new Set();

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      const current = maps[r][c];

      if (current !== 'L') continue;

      LToE.push([r, c, 0]);
      visited.add([r, c].join(':'));
      let idx = 0;

      while (idx < LToE.length) {
        const sr = LToE[idx][0];
        const sc = LToE[idx][1];
        const count = LToE[idx][2];
        idx += 1;

        if (maps[sr][sc] === 'E') {
          LToECount = count;
          break;
        };

        for (let d of direction) {
          const nr = sr + d[0];
          const nc = sc + d[1];

          if (nr < 0 || nr >= height || nc < 0 || nc >= width) continue;

          if (visited.has([nr, nc].join(':'))) continue;

          if (maps[nr][nc] === 'X') continue;

          LToE.push([nr, nc, count + 1]);
          visited.add([nr, nc].join(':'));
        };
      };
    };
  };

  if (LToECount === -1) return -1;

  const SToL = [];
  visited.clear();
  

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      const current = maps[r][c];

      if (current !== 'S') continue;

      SToL.push([r, c, 0]);
      visited.add([r, c].join(':'));
      let idx = 0;

      while (idx < SToL.length) {
        const sr = SToL[idx][0];
        const sc = SToL[idx][1];
        const count = SToL[idx][2];
        idx += 1;

        if (maps[sr][sc] === 'L') {
          SToLCount = count;
          break;
        };

        for (let d of direction) {
          const nr = sr + d[0];
          const nc = sc + d[1];

          if (nr < 0 || nr >= height || nc < 0 || nc >= width) continue;

          if (visited.has([nr, nc].join(':'))) continue;

          if (maps[nr][nc] === 'X') continue;

          SToL.push([nr, nc, count + 1]);
          visited.add([nr, nc].join(':'));
        };
      };
    };
  };

  if (SToLCount === -1) return -1;

  answer = SToLCount + LToECount;

  return answer;
};

console.log(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]));
console.log(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]));