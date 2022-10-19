function solution(num, total) {
  var answer = [];
  const middle = parseInt(total / num);
  const halfCount = parseInt(num / 2);
  let start;
  
  if (num % 2 === 1) {
    start = middle - halfCount
  } else {
    start = middle - halfCount + 1
  }

  for (let i = 0; i < num; i++) {
    answer.push(start + i)
  }

  return answer;
}