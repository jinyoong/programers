function solution(array, n) {
  let answer = 0;
  let different = 987654321;

  array.map(element => {
    const elementDiff = Math.abs(element - n)

    if (elementDiff < different) {
      answer = element;
      different = elementDiff;
    } else if (elementDiff === different && element < answer) {
      answer = element;
    }
  })

  return answer;
}