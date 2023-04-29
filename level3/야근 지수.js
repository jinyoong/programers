function solution(n, works) {
  let answer = 0;
  const total = works.reduce((acc, cur) => acc + cur, 0);
  const count = works.length;

  if (total <= n) {
    return answer;
  };

  const deleteN = total - n;
  const average = parseInt(deleteN / count);
  const remainCount = deleteN - average * count;
  
  answer += average ** 2 * count;
  answer += (2 * average + 1) * remainCount;
  
  return answer;
};

console.log(solution(4, [4, 3, 3]));
console.log(solution(1, [2, 1, 2]));
console.log(solution(3, [2, 2, 2]));
console.log(solution(999, [800, 100, 55, 45]));
console.log(solution(99, [2, 15, 22, 55, 55]));