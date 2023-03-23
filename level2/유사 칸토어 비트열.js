function solution(n, l, r) {
  let answer = r - l + 1;
  let numberCount = [[], [2]]
  let isBreak = false;

  for (let i = 2; i <= n; i++) {
    let newCount = [];

    if (isBreak) {
      break;
    };

    for (let j = 0; j < 5; j++) {
      if (newCount[newCount.lentgh - 1] >= r) {
        isBreak = true;
        break;
      };

      if (j === 2) {
        newCount.push(...new Array(5 ** (i - 1)).fill(0).map((element, index) => 5 ** (i - 1) * 2 + index));
      } else {
        newCount.push(...numberCount[i - 1].map(element => element + (5 ** (i - 1) * j)))
      };
    };

    numberCount.push(newCount);
  };

  let targetArray = numberCount[n];
  console.log(targetArray);

  targetArray.forEach(number => {
    if (number >= l && number < r) {
      answer -= 1;
    };
  });

  return answer;
}

`
1
11011 => 1101111011000001101111011
00000 => 0000000000000000000000000

11011 => A로, 00000 => B로 치환하면
A => AABAA, B => BBBBB로 변한다

0: 1, 1개
1: A, 5개, 2
2: AABAA, 25개, 1번째 위치 + 5 * (0, 1, 3, 4) + 5 ^ (n - 1) * 2 ~ (5 ^ (n - 1)) - 1 
3: CCDCC, 125개, 2번째 위치 + 5 * (0, 1, 3, 4) + 5 ^ (n - 1) * 2 ~ (5 ^ (n - 1)) - 1 
4: EEFEE
`

console.log(solution(2, 4, 17));
console.log(solution(0, 0, 0));
console.log(solution(1, 0, 4));
console.log(solution(3, 0, 10));
console.log(solution(20, 0, 50));