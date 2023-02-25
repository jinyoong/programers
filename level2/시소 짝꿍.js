function solution(weights) {
  let answer = 0;
  let array = new Array(901).fill(0);
  let weightArray = new Array();

  weights.forEach(weight => {
    array[weight - 100] += 1;

    if (array[weight - 100] === 1) {
      weightArray.push(weight);
    };
  });

  let sortedWeights = weightArray.sort((a, b) => a - b);

  for (let i = 0; i < sortedWeights.length; i++) {
    const standard = sortedWeights[i];
    const standardCount = array[standard - 100];

    answer += parseInt(standardCount * (standardCount - 1) / 2);

    for (let j = i + 1; j < sortedWeights.length; j++) {
      const target = sortedWeights[j];
      const targetCount = array[target - 100];

      if (target > standard * 2) break;

      [[1, 2], [2, 3], [3, 4]].forEach(element => {
        const x = element[0];
        const y = element[1];

        if (target * x === standard * y) answer += standardCount * targetCount
      });
    };
  };

  return answer;
};

console.log(solution([100, 180, 360, 100, 270]));
console.log(solution([100, 100, 100, 100]));
console.log(solution([100, 100, 100, 200, 200]));
console.log(solution([100, 100, 150, 200]));
console.log(solution([100, 100]));
console.log(solution([100, 100, 100, 200, 200, 200]));
console.log(solution([100, 100, 100, 200, 200, 300, 400]));
console.log(solution([100, 100, 100, 100, 100, 100, 100]));