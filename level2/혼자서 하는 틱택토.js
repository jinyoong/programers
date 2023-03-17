function solution(board) {
  let answer = 0;
  let position = {
    'O': [],
    'X': [],
  };

  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      const element = board[r][c];
      
      if (element === '.') {
        continue;
      };

      position[element].push([r, c]);
    };
  };

  if (position['O'].length < position['X'].length) {
    return answer;
  };

  let visited = {
    'O': new Array(position['O'].length).fill(0),
    'X': new Array(position['X'].length).fill(0),
  };

  let turnArray = ['O', 'X'];
  let isPossible = false;
  let gameBoard = new Array(3).fill(0).map(() => new Array(3).fill('.'));

  function game(turnIdx, result) {
    const turn = turnArray[turnIdx];

    if (visited['O'].every(element => element === 1) && visited['X'].every(element => element === 1)) {
      answer = 1;
      isPossible = true;
      return;
    };

    if (!check(result)) {
      return;
    };

    for (let idx = 0; idx < position[turn].length; idx++) {
      if (visited[turn][idx] === 1) {
        continue;
      };

      const r = position[turn][idx][0];
      const c = position[turn][idx][1];

      visited[turn][idx] = 1;
      result[r][c] = turn;
      game((turnIdx + 1) % 2, result);
      visited[turn][idx] = 0;
      result[r][c] = '.';

      if (isPossible) {
        return;
      };
    };
  };

  game(0, gameBoard);

  return answer;
}

function check(gameBoard) {
  for (let i = 0; i < 3; i++) {
    if (gameBoard[i][0] === gameBoard[i][1] && gameBoard[i][1] === gameBoard[i][2] && gameBoard[i][1] !== '.') {
      return false;
    };

    if (gameBoard[0][i] === gameBoard[1][i] && gameBoard[1][i] === gameBoard[2][i] && gameBoard[1][i] !== '.') {
      return false;
    };
  };

  if (gameBoard[0][0] === gameBoard[1][1] && gameBoard[1][1] === gameBoard[2][2] && gameBoard[1][1] !== '.') {
    return false;
  };

  if (gameBoard[0][2] === gameBoard[1][1] && gameBoard[1][1] === gameBoard[2][0] && gameBoard[1][1] !== '.') {
    return false;
  };

  return true;
}

const data = [
  [["OXO", "XOX", "OXO"], 1],
  [["OOX", "XXO", "OOX"], 1],
  [["XXX", ".OO", "O.."], 1],
  [["OX.", ".O.", ".XO"], 1],
  [["...", "...", ".O."], 1],
  [["X.X", "X.O", "O.O"], 1],
  [["XO.", "OXO", "XOX"], 1],
  [["OOO", "XOX", "XXO"], 1],
  [["OOO", "XOX", "X.X"], 0],
  [["XXX", "OO.", "OO."], 0],
  [[".X.", "...", "..."], 0],
  [[".X.", "X..", ".O."], 0],
  [["XOX", "OXO", "XOX"], 0],
  [["XXX", "XOO", "OOO"], 0],
  [["OOX", "OXO", "XOO"], 0],
  [["OOX", "OXO", "XOX"], 0],
  [[".OX", "OXO", "XO."], 0],
  [["OOO", "XX.", "X.."], 0],
  [["OOX", "XXO", "OXO"], 1],
  [["XXX", "XXX", "XXX"], 0],
  [["OOO", "OOO", "OOO"], 0],
  [["OXO", ".XO", "X.O"], 1],
  [["OOO", "X.X", "..."], 1],
  [["OOO", "...", "..."], 0],
  [["O..", "...", "..."], 1],
  [[".O.", "...", "..."], 1],
  [["..O", "...", "..."], 1],
  [["...", "O..", "..."], 1],
  [["...", ".O.", "..."], 1],
  [["...", "..O", "..."], 1],
  [["...", "...", "O.."], 1],
  [["...", "...", ".O."], 1],
  [["...", "...", "..O"], 1],
  [["X..", "...", "..."], 0],
  [[".X.", "...", "..."], 0],
  [["..X", "...", "..."], 0],
  [["...", "X..", "..."], 0],
  [["...", ".X.", "..."], 0],
  [["...", "..X", "..."], 0],
  [["...", "...", "X.."], 0],
  [["...", "...", ".X."], 0],
  [["...", "...", "..X"], 0],
  [["OX.", ".OX", "..O"], 1],
  [["O..", ".O.", "..O"], 0],
  [["X..", ".X.", "..X"], 0],
  [["XO.", "XO.", "XO."], 0],
  [["XO.", "...", "..."], 1],
  [["OXO", "...", "..."], 1],
  [["OXO", "X..", "..."], 1],
  [["OXO", "XO.", "..."], 1],
  [["OOO", "X.X", ".X."], 0],
  [["OOO", "X.X", "XX."], 0],
  [["XXX", "OO.", ".OO"], 0],
  [["XO.", "OXO", "XOX"], 1],
  [["OOO", "XOX", "XXO"], 1],
  [["OOO", "OOX", "XXX"], 0],
  [["XOX", "OXO", "XOX"], 0],
  [["XXO", "OOX", "XO."], 1],
  [["XXO", "OOX", "XOO"], 1],
  [["X.X", ".X.", "X.X"], 0],
  [[".X.", "X.X", ".X."], 0],
  [["O.O", ".O.", "O.O"], 0],
  [[".O.", "O.O", ".O."], 0],
  [["OX.", "OXO", ".XO"], 0],
  [["OX.", "OX.", ".XO"], 1],
  [["OX.", "OXO", "XXO"], 1],
  [["OX.", "...", "..."], 1],
  [["...", "...", "OX."], 1],
  [["OXO", "XOX", "OXO"], 1],
  [["OOX", "XXO", "OOX"], 1],
  [["XXX", ".OO", "O.."], 1],
  [["OX.", ".O.", ".XO"], 1],
  [["X.X", "X.O", "O.O"], 1],
  [["XO.", "OXO", "XOX"], 1],
  [["OOO", "XOX", "X.X"], 0],
  [["XXX", "OO.", "OO."], 0],
  [[".X.", "X..", ".O."], 0],
  [["XXX", "XOO", "OOO"], 0],
  [["OOX", "OXO", "XOO"], 0],
  [["OOX", "OXO", "XOX"], 0],
  [[".OX", "OXO", "XO."], 0],
  [["OOO", "XX.", "X.."], 0],
];

data.forEach((dataElement, index) => {
  const testCase = dataElement[0];
  const answer = dataElement[1];

  if (solution(testCase) === answer) {
    console.log(`${index + 1}번 정답`);
  } else {
    console.log(`${index + 1}번 오답`);
    console.log(testCase, answer);
  }
});