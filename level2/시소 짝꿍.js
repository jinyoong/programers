function solution(weights) {
  let answer = 0;
  let sortedWeights = weights.sort();
  
  for (let i = 0; i < sortedWeights.length - 1; i++) {
    const standard = sortedWeights[i];

    for (let j = i + 1; j < sortedWeights.length; j++) {
      const target = sortedWeights[j];

      if (target > standard * 2) break;

      if (target === standard) answer += 1;
      
      if (target === standard * 2) answer += 1;

      if (target * 2 === standard * 3) answer += 1;

      if (target * 3 === standard * 4) answer += 1;

    };
  };

  return answer;
};

console.log(solution([100, 180, 360, 100, 270]));
console.log(solution([100, 100, 100, 100]));