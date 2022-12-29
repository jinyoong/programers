function solution(n) {
  let answer = 0;

  for (let i = 1; i <= parseInt(n ** 0.5); i++) {

    answer += (n % i === 0) ? (i * i === n) ? 1 : 2 : 0

  }
  
  return answer;
}