function solution(balls, share) {
  let answer = 0;
  let big;
  let small;

  if (balls - share > share) {
    big = balls - share
    small = share
  } else {
    big = share
    small = balls - share
  }

  let top = 1;
  for (let i = balls; i > big; i--) {
    top *= i
  }
  let bottom = 1;
  for (let i = small; i > 0; i--) {
    bottom *= i
  }

  answer = parseInt(top / bottom)

  return answer;
}