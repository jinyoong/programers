function solution(dots) {
  var answer = 0;
  let w;
  let h;
  let x = dots[0][0];
  let y = dots[0][1];

  for (let i = 1; i < 4; i++) {
    if (dots[i][0] != x) {
      w = Math.abs(dots[i][0] - x)
    }

    if (dots[i][1] != y) {
      h = Math.abs(dots[i][1] - y)
    }
  }

  answer += w * h
  return answer;
}