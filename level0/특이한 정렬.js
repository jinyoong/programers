function solution(numlist, n) {
  let answer = [];
  let numbers = new Array(10001).fill(0);

  numlist.forEach(num => {
    numbers[num] = 1
  })

  let diff = 0;
  while (answer.length != numlist.length) {
    let plus = n + diff;
    let minus = n - diff;

    if (diff === 0) {
      if (numbers[n] === 1){
        answer.push(n)
      }
    } else {
      if (numbers[plus] === 1) {
        answer.push(plus)
      }

      if (numbers[minus] === 1) {
        answer.push(minus)
      }
    }
    diff += 1
  }
  return answer;
}