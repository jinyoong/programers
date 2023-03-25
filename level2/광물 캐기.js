function solution(picks, minerals) {
  const totalPicks = picks[0] + picks[1] + picks[2];
  let answer = 0;
  let powers = [[1, 1, 1], [5, 1, 1], [25, 5, 1]];
  let expect = [];
  let count = [0, 0, 0];
  let needPicks = [0, 0, 0]

  for (let index = 0; index < minerals.length; index++) {
    const mineral = minerals[index];

    if (index >= 5 * totalPicks) {
      break;
    };

    if (index % 5 === 0 && index !== 0) {
      const mineralMax = Math.max(...count);
      const maxIndex = count.indexOf(mineralMax);
      expect.push([maxIndex, ...count]);
      needPicks[maxIndex] += 1;
      count = [0, 0, 0];
    };

    switch (mineral) {
      case "diamond":
        count[0] += 1;
        break;
      case "iron":
        count[1] += 1;
        break;
      default:
        count[2] += 1;
    };
  };

  const mineralMax = Math.max(...count);
  const maxIndex = count.indexOf(mineralMax);
  expect.push([maxIndex, ...count]);
  needPicks[maxIndex] += 1;
  
  console.log(expect);
  console.log(picks);
  console.log(needPicks);

  function check() {
    if (count.every(element => element === 0)) {
      return 0;
    };
  
    const mineralMax = Math.max(...count);
    const diaCount = count[0];
    const ironCount = count[1];
    const stoneCount = count[2];
    let result = 0;
  
    if (count[0] === mineralMax) {
      if (picks[0] !== 0) {
        result = diaCount + ironCount + stoneCount;
      } else {  
        for (let i = 1; i < 3; i++) {
          if (picks[i] !== 0) {
            result = powers[i][0] * diaCount + powers[i][1] * ironCount + powers[i][2] * stoneCount;
            break;
          };
        };
      };
    } else if (count[1] === mineralMax) {
      
    }
  };

  return answer;
};


console.log(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]));
console.log(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]));