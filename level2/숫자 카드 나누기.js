function solution(arrayA, arrayB) {
  var answer = 0;
  let arrayAGcd = arrayA[0];
  let arrayBGcd = arrayB[0];

  for (let i = 1; i < arrayA.length; i++) {
    arrayAGcd = gcd(arrayAGcd, arrayA[i]);
    arrayBGcd = gcd(arrayBGcd, arrayB[i]);
  };

  answer = check(answer, arrayB, arrayAGcd);
  answer = check(answer, arrayA, arrayBGcd);

  return answer;
};

function gcd(num1, num2) {
  let x = 0;
  let y = 0;

  if (num1 > num2) {
    x = num1;
    y = num2;
  } else {
    x = num2;
    y = num1;
  }

  while (y > 0) {
    let temp = y;
    y = x % y;
    x = temp;
  }

  return x;
};

function check(maximum, targetArray, target) {
  if (target === 1 || target <= maximum) return maximum;

  for (let number = target; target > 0; target--) {
    if (number <= maximum) break;

    if (target % number !== 0) continue;

    if (targetArray.filter(element => element % number !== 0).length === targetArray.length) return number;
  };

  return 0;
};

console.log(solution([10, 17], [5, 20]));
console.log(solution([10, 20], [5, 17]));
console.log(solution([14, 35, 119], [18, 30, 102]));