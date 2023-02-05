function solution(n) {
  let answer = 0;

  function chess(board, idx, n) {
    if (idx === n) {
      answer += 1;
      return;
    };
  
    for (let c = 0; c < n; c++) {
      if (board[idx][c] === 1) continue;
  
      const copyBoard = new Array(n).fill(0).map((element, index) => [...board[index]]);
  
      copyBoard[idx][c] = 1;
      for (let i = 1; i < n; i++) {
        const nr = idx + i;
        const leftSide = c - i;
        const rightSide = c + i;
  
        if (nr >= n) break;
        
        copyBoard[nr][c] = 1;
  
        if (leftSide >= 0) {
          copyBoard[nr][leftSide] = 1;
        };
  
        if (rightSide < n) {
          copyBoard[nr][rightSide] = 1;
        };
      };
      chess(copyBoard, idx + 1, n);
    };
  };

  chess(new Array(n).fill(0).map(() => new Array(n).fill(0)), 0, n);
  
  return answer;
};

console.log(solution(5))