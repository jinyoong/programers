function solution(begin, end) {
  let answer = [];

  for (let number = begin; number <= end; number++) {
    answer.push(calculate(number));
  }

  return answer;
};

function calculate(number) {
  if (number === 1) return 0;

  let result = 1;

  const maximum = Math.ceil(Math.sqrt(number));

  for (let i = 2; i <= maximum; i++) {
    
    if (number % i !== 0) continue;

    if (parseInt(number / i) <= 10000000) {
      result = parseInt(number / i);
      break;
    } else {
      result = i;
    };
  };

  return result;
};

// console.log(solution(900, 920));
// console.log(solution(999999990, 1000000000))
console.log(solution(100000014, 100000016))