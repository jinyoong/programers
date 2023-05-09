function solution(n, s) {
  let answer = [];

  if (n > s) {
    answer.push(-1);
    return answer;
  };

  const target = parseInt(s / n);
  const remain = s % n;

  answer = new Array(n).fill(target);

  for (let i = n - remain; i < n; i++) {
    answer[i] += 1;
  }

  return answer;
}

console.log(solution(2, 9));
console.log(solution(2, 1));