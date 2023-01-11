function solution(bin1, bin2) {
  let answer = '';
  const length1 = bin1.length;
  const length2 = bin2.length;
  const max_length = Math.max(length1, length2);
  const number1 = bin1.padStart(max_length, "0");
  const number2 = bin2.padStart(max_length, "0")

  let upperNumber = 0;

  for (let i = max_length - 1; i >= 0; i--) {
    const target = upperNumber + Number(number1[i]) + Number(number2[i]);

    if (target >= 2) {
      upperNumber = 1;
    } else {
      upperNumber = 0;
    }

    answer = String(target % 2) + answer;
  }

  if (upperNumber === 1) {
    answer = String(upperNumber) + answer;
  }

  return answer;
}

console.log(solution("0", "0"))
console.log(solution("10", "1011"))