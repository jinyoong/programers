function solution(sticker) {
  let answer = 0;
  let dpFirst = new Array(sticker.length + 1).fill(0);
  let dpSecond = new Array(sticker.length + 1).fill(0);

  if (sticker.length === 1) {
    answer = sticker[0];
    return answer;
  }

  // 0번 스티커를 뜯는 경우 => 마지막 스티커는 뜯을 수 없다
  dpFirst[1] = sticker[0];
  for (let i = 2; i < dpFirst.length - 1; i++) {
    dpFirst[i] = Math.max(dpFirst[i - 2] + sticker[i - 1], dpFirst[i - 1]);
  }

  // 1번 스티커를 뜯는 경우 => 마지막 스티커를 뜯을 수 있다.
  for (let i = 2; i < dpFirst.length; i++) {
    dpSecond[i] = Math.max(dpSecond[i - 2] + sticker[i - 1], dpSecond[i - 1]);
  }

  answer = Math.max(dpFirst[dpFirst.length - 2], dpSecond[dpSecond.length - 1]);

  return answer;
}

console.log(solution([14, 6, 5, 11, 3, 9, 2, 10]));
console.log(solution([1, 3, 2, 5, 4]));
console.log(solution([1]));
console.log(solution([1, 3]));