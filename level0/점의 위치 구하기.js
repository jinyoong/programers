function solution(dot) {
  var answer = 0;
  const x = dot[0];
  const y = dot[1];

  if (x > 0  && y > 0) {
    answer = 1
  } else if (x > 0 && y < 0) {
    answer = 4
  } else if (x < 0 && y > 0) {
    answer = 2
  } else {
    answer = 3
  }

  return answer;
}