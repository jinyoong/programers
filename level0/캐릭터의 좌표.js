function solution(keyinput, board) {
  let answer = [0, 0];
  const direction = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]};
  const width = board[0];
  const height = board[1];

  keyinput.forEach(key => {
    let r = answer[0];
    let c = answer[1];
    let nr = r + direction[key][0];
    let nc = c + direction[key][1];

    if (nr < -1 * parseInt(width / 2) || nr > parseInt(width / 2) || nc < -1 * parseInt(height / 2) || nc > parseInt(height / 2)) {
      return;
    } else {
      answer[0] = nr;
      answer[1] = nc;
    }

  })

  return answer;
}