function solution(n, s) {
  let answer = [];
  let number = s;

  if (n > s) {
    answer.push(-1);
    return answer;
  };

  for (let i = 0; i < n; i++) {
    const count = n - i;
    const target = parseInt(number / count);

    answer.push(target);
    number -= target;
  };

  return answer;
}

console.log(solution(2, 9));
console.log(solution(2, 1));