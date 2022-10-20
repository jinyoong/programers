function solution(sides) {
  let answer = 0;
  let big;
  let small;

  if (sides[0] >= sides[1]) {
    big = sides[0];
    small = sides[1];
  } else {
    big = sides[1];
    small = sides[0];
  }

  // 1. sides에서 더 큰 수를 가장 긴 변으로 할 경우 => 추가 되는 변은 big 보다 작아야 한다
  
  for (let newSide = big - 1; newSide >= 0; newSide--) {
    if (newSide + small <= big) {
      break
    } else {
      answer += 1
    }
  }

  // 2. sides에 추가될 수를 가장 긴 변으로 할 경우
  answer += small

  return answer;
}