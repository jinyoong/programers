function solution(s) {
  let answer = 1;
  let wordLength = s.length;
  let dp = new Array(s.length).fill(0).map(() => new Array(s.length).fill(false));
  // dp[i][j] : i번째 글자부터 j번째 글짜까지가 팰린드롬인지 여부

  for (let i = 0; i < wordLength; i++) {
    dp[i][i] = true;
  };

  for (let i = 0; i < wordLength - 1; i++) {
    if (s[i] === s[i + 1]) {
      dp[i][i + 1] = true;
    };
  };

  for (let interval = 3; interval < wordLength + 1; interval++) {
    for (let start = 0; start < wordLength - interval + 1; start++) {
      const end = start + interval - 1;
      if (s[start] === s[end] && dp[start + 1][end - 1]) {
        dp[start][end] = true;
        answer = interval;
      };
    };
  };

  return answer;
};

console.log(solution("abcdcba"));
console.log(solution("abacde"));