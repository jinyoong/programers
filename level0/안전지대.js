function solution(board) {
  var answer = 0;
  const directionArray = [
    [-1, -1], [-1, 0], [-1, 1], [0, 1],
    [1, 1], [1, 0], [1, -1], [0, -1]
  ]
  const n = board.length
  
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {

      if (board[r][c] != 1) {
        continue
      }

      for (let i = 0; i < 8; i++) {
        let nr = r + directionArray[i][0];
        let nc = c + directionArray[i][1];

        if (nr < 0 || nr >= n || nc < 0 || nc >= n) {
          continue
        }

        if (board[nr][nc] == 1) {
          continue
        }

        board[nr][nc] = 2
      }

    }
  }

  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (board[r][c] == 0) {
        answer += 1
      }
    }
  }

  return answer;
}