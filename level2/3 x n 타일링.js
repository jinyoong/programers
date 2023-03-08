function solution(n) {
  let answer = 0;

  if (n % 2 === 1) {
    return answer;
  };

  const dp = new Array(parseInt(n / 2) + 1).fill('0');

  dp[0] = '1';
  dp[1] = '3';

  for (let i = 2; i <= parseInt(n / 2); i++) {
    dp[i] = String(Number(dp[i - 1] * 4) - Number(dp[i - 2]));
  };

  answer = Number(dp[parseInt(n / 2)]) % 1000000007;
  return answer;
};

console.log(solution(5000));