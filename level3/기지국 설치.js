function solution(n, stations, w) {
  let answer = 0;
  let start = 1;
  let targets = new Array();

  for (let station of stations) {
    const left = station - w;
    const right = station + w;
    const target = left - start;
    start = right + 1;

    targets.push(target);
  };

  if (start <= n) {
    targets.push(n - start + 1);
  };

  for (let target of targets) {
    answer += Math.ceil(target / (2 * w + 1));
  }

  return answer;
};

console.log(solution(11, [4, 11], 1));
console.log(solution(11, [4, 9], 1));
console.log(solution(16, [9], 2));