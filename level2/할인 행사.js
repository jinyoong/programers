function solution(want, number, discount) {
  var answer = 0;
  const dict = new Object();
  const numberArray = new Array(number.length).fill(0);

  want.map((element, idx) => {
    dict[element] = idx;
  });

  for (let i = 0; i < discount.length; i++) {
    const numberIdx = dict[discount[i]];
    numberArray[numberIdx] += 1

    if (i >= 10) {
      const deleteIdx = dict[discount[i - 10]]
      numberArray[deleteIdx] -= 1
    }

    if (check(number, numberArray)) {
      answer += 1
    }
  }

  return answer;
}

function check(number, target) {
  let isCheck = true;

  target.map((element, idx) => {
    if (element < number[idx]) {
      isCheck = false;
      return;
    }
  })

  return isCheck;
}

console.log(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]));