function solution(grid) {
  let answer = [];
  let width = grid[0].length;
  let height = grid.length;
  let visited = new Array(height).fill(0).map(() => new Array(width).fill(0));
  let directions = [[0, -1], [-1, 0], [0, 1], [1, 0]];
  let match = {'S': 0, 'R': 3, 'L': 1};
  // visited[i][j] : i행, j열로 들어온 빛의 이전 방향을 저장. 1 : 왼쪽, 3 : 아래쪽, 5 : 오른쪽, 7 : 위쪽
  // 즉, visited[i][j] = 10 이면 가능한 건 왼쪽(1) 과 오른쪽(5) 이게 된다.

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      const possibleDirection = findPossibleDirection(visited[r][c]);

      for (let element of possibleDirection) {

      }
    }
  }

  function cycle(sr, sc, direction) {
  }

  return answer;
}

function findPossibleDirection(point) {
  let result = [];

  function req(num, sum, subResult) {
    if (sum > 16) {
      return;
    }

    if (sum === 16) {
      result = [...subResult];
      return;
    }

    for (let i = num; i <= 7; i += 2) {
      
      req(num + 2, sum + num, [...subResult, num]);
    }
  }

  req(1, point, []);

  return new Set(result);
}

console.log(solution(["SL","LR"]));
console.log(solution(["S"]));
console.log(solution(["R","R"]));