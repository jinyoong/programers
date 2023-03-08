function solution(n) {
  let answer = 0;

  if (n % 2 === 1) {
    return answer;
  };

  const dp = new Array(parseInt(n / 2) + 1).fill(0);
  const MOD = 1000000007;

  dp[0] = 1;
  dp[1] = 3;

  for (let i = 2; i <= parseInt(n / 2); i++) {
    const modResult = (((dp[i - 1] * 4) % MOD) - (dp[i - 2] % MOD) + MOD) % MOD;
    dp[i] = modResult;
  };

  answer = dp[parseInt(n / 2)];
  return answer;
};

console.log(solution(4000));