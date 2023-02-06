function solution(begin, end) {
  let answer = [];

  for (let number = begin; number <= end; number++) {
    answer.push(calculate(number));
  }

  return answer;
};

function calculate(number) {
  if (number === 1) return 0;

  const maximum = Math.ceil(Math.sqrt(number));

  for (let i = 2; i <= maximum; i++) {
    if (parseInt(number / i) <= 10000000 && number % i === 0) return parseInt(number / i);
  };

  return 1;
};

console.log(solution(900, 920));
console.log(solution(999999999, 1000000000))