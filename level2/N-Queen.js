function solution(n) {
  let answer = 0;

  function chess(before, column, idx, n) {
    const current = new Array(n).fill(0);

    if (idx === n) {
      answer += 1;
      return;
    };
  
    for (let c = 0; c < n; c++) {
      if (column[c] === 1) {
        continue;
      };
  
      if ((c - 1) >= 0 && before[c - 1] === 1) {
        current[c] = 1;
        continue;
      };
  
      if (c + 1 < n && before[c + 1] === 1) {
        current[c] = 1;
        continue;
      };
  
      current[c] = 1;
      column[c] = 1;
      chess(current, column, idx + 1, n)
      current[c] = 0;
      column[c] = 0;
    };
  };

  chess(new Array(n).fill(0), new Array(n).fill(0), 0, n);

  return answer;
};

console.log(solution(5))