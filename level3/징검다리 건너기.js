function solution(stones, k) {
  let left = 0;
  let right = 200000000;
  let middle;

  while (left <= right) {
    middle = parseInt((left + right) / 2);
    let impossibleCount = 0;
    let isBig = false;

    for (let i = 0; i < stones.length; i++) {
      if (stones[i] <= middle) {
        impossibleCount += 1;
      } else {
        impossibleCount = 0;
      };

      if (impossibleCount === k) {
        isBig = true;
        break;
      };
    };

    if (isBig) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  };

  return left;
};

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
console.log(solution([200, 100, 1, 50], 2));
console.log(solution([3, 1, 2, 1], 3));