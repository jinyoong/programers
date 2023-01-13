function solution(lines) {
  let answer = 0
  const board = new Array(250).fill(0);

  for (let line of lines) {
    const start = line[0];
    const end = line[1];

    for (let i = start; i < end; i++) {
      board[i + 100] += 1
    }
  }

  for (let i = 0; i < 250; i++) {
    if (board[i] >= 2) answer += 1;
  }
  
  return answer
}