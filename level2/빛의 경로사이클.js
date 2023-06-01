function solution(grid) {
  let answer = [];
  let width = grid[0].length;
  let height = grid.length;
  let visited = new Array(height).fill(0).map(() => new Array(width).fill(0));
  let directions = [[0, -1], [-1, 0], [0, 1], [1, 0]];
  let match = {'S': 0, 'R': 3, 'L': 1};
  // visited[i][j] : i행, j열로 들어온 빛의 이전 방향을 저장.
  // 10^0 : 왼쪽, 10^1 : 위쪽, 10^2 : 오른쪽, 10^3 : 아래쪽
  // vistied[1][1] = 1010 : 1행 1열에는 빛이 아래쪽, 위쪽 두 방향에서 왔었다.
  
  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      for (let p = 0; p < 4; p++) {
        if (numberOfPlace(visited[r][c], p) === 0) {
          let result = cycle(r, c, p, 0);
          answer.push(result);
        }
      }
    }
  }

  function cycle(sr, sc, sd, result) {
    let d = sd;
    let r = sr;
    let c = sc;

    do {
      if (numberOfPlace(visited[r][c], d) === 0) {
        visited[r][c] += 10 ** d;
      }

      const gridElement = grid[r][c];
      const direction = directions[(d + match[gridElement]) % 4];
      d = (d + match[gridElement]) % 4;
      r = calculateLocation(r + direction[0], height);
      c = calculateLocation(c + direction[1], width);

      result += 1;
    } while (!(r === sr && c === sc && d === sd));

    return result;
  }

  return answer.sort((a, b) => a - b);
}

function calculateLocation(input, limit) {
  const result = (input + limit) % limit;

  return result;
}

function numberOfPlace(number, d) {
  let result = 0;
  
  if (d === 0) {
    result = number % 10;  
  } else {
    result = parseInt((number / (10 ** d)) % 10);
  }

  return result;
}

// console.log(solution(["SL","LR"]));
// console.log(solution(["S"]));
// console.log(solution(["R","R"]));
// console.log(solution(["RR", "RR"]));
console.log(solution(['S', 'S']))