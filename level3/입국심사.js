function solution(n, times) {
  let answer = 0;
  let minTime = 0;
  let maxTime = Math.min(...times) * n;

  while (minTime <= maxTime) {
    let middle = parseInt((minTime + maxTime) / 2);
    if (checkInTime(middle, n, times) === 'left') {
      maxTime = middle - 1;
    } else {
      minTime = middle + 1;
    }
  }

  answer = minTime;
  return answer;
}

function checkInTime(target, n,  times) {
  let result = 0;

  times.forEach(time => {
    result += parseInt(target / time);
  })

  if (n <= result) {
    return 'left';
  } else {
    return 'right';
  }
}

console.log(solution(6, [7, 10]));
console.log(solution(5, [1, 1, 1, 1, 2]));