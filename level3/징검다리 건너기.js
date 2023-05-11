function solution(stones, k) {
  let answer = 0;
  let peoples = new Array(stones.length).fill(0);

  peoples[0] = stones[0];
  stones[0] = 0;

  for (let i = 1; i < stones.length + 1; i++) {

    if (i === stones.length) {
      for (let j = 1; j <= k; j++) {
        const idx = i - j;
        
        if (idx < 0) {
          break;
        };

        answer += peoples[idx];
      };

      break;
    };

    let maximum = stones[i];

    for (let j = 1; j <= k; j++) {
      const idx = i - j;

      if (idx >= 0) {
        const people = peoples[idx];
        const possible = Math.min(people, maximum);

        peoples[idx] -= possible;
        maximum -= possible; 
        peoples[i] += possible;
      } else {
        peoples[i] += maximum;
        maximum = 0;
      };

      if (maximum === 0) {
        break;
      };
    };

    console.log(...peoples);
    console.log(...stones);
    console.log("=================")
  };

  return answer;
};

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
console.log(solution([3, 1, 2, 1], 3));