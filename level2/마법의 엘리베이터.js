function solution(storey) {
  let answer = 0;
  const target = [...String(storey).split('').reverse(), '0'];

  target.forEach((element, index) => {
    const current = Number(element);
    const nextNumber = Number(target[index + 1]);

    if (current < 5) {
      answer += current;
    }
    else if (current > 5) {
      answer += 10 - current;
      target[index + 1] = String(nextNumber + 1);
    }
    else {
      if (nextNumber + 1 <= 5) {
        answer += current;
      }
      else {
        answer += 10 - current;
        target[index + 1] = String(nextNumber + 1);
      }
    }
  });

  return answer;
}

console.log(solution(16))
console.log(solution(2554))