function solution(num, k) {
  let answer = num.toString().split("").findIndex(element => element === String(k));
  return answer + (answer === -1 ? 0 : 1);
}