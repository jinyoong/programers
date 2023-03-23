function solution(n, l, r) {
  let answer = r - l + 1;
  let target = [2];
  let isBreak = false;

  for (let i = 2; i <= n; i++) {
    let newTarget = [];

    if (isBreak === true) {
      break;
    };

    for (j = 0; j < 5; j++) {
      if (j === 2) {
        for (let k = 0; k < 5 ** (i - 1); k++) {
          const number = 5 ** (i - 1) * j + k;

          if (number >= r) {
            isBreak = true;
            break;
          };

          newTarget.push(number);
        };
      } else {
        for (let element of target) {
          const number = element + 5 ** (i - 1) * j;
          
          if (number >= r) {
            isBreak = true;
            break;
          };

          newTarget.push(number);
        };
      };
    };

    target = [...newTarget];
  };

  console.log(target);

  target.forEach(number => {
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

2
2, 7, 10, 11, 12, 13, 14, 17, 22
2, 7, 10, 11, 12, 13, 14, 17, 22, 27, 32, 35, 36, 37, 38, 39, 42, 47, 50, 

0, 1, 3, 4
0, 1, 3, 4, 5, 6, 8, 9, 
`

console.log(solution(2, 4, 17));
console.log(solution(1, 0, 4));
console.log(solution(3, 70, 125));
console.log(solution(20, 9000, 10000));