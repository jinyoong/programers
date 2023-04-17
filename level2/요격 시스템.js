function solution(targets) {
  let answer = 0;
  let result = [];
  let sortedTargets = targets.sort((a, b) => a[0] - b[0]);

  for (let i = 0; i < sortedTargets.length; i++) {
    const target = sortedTargets[i];
    const targetS = target[0];
    const targetE = target[1];

    if (result.length === 0) {
      result.push(target);
    } else {
      let isIn = false;

      for (let j = 0; j < result.length; j++) {
        const element = result[j];
        const elementS = element[0];
        const elementE = element[1];

        if (elementS >= targetE || elementE <= targetS) {
          continue;
        };

        const newS = Math.max(elementS, targetS);
        const newE = Math.min(elementE, targetE);
        
        result[j] = [newS, newE];
        isIn = true;
        break;
      };

      if (!isIn) {
        result.push(target);
      };
    };
  };

  answer = result.length;

  return answer;
};

console.log(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]));
console.log(solution([[1, 2], [2, 3], [3, 4], [3, 5], [4, 5]]));
console.log(solution([[0,4],[5,10],[6,8],[8,9]]));
console.log(solution([[0, 4], [1, 2], [1, 3], [3, 4]]));
console.log(solution([[0, 4], [0, 1], [2, 3]]));