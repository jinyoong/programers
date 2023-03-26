function solution(picks, minerals) {
  const totalPicks = picks[0] + picks[1] + picks[2];
  let answer = totalPicks * 125;
  let expect = [];
  let count = [0, 0, 0];

  for (let index = 0; index < minerals.length; index++) {
    const mineral = minerals[index];

    if (index >= 5 * totalPicks) {
      break;
    };

    if (index % 5 === 0 && index !== 0) {
      expect.push(makeCase(count));
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

  expect.push(makeCase(count));

  function req(idx, remains, result) {
    if (result >= answer) {
      return;
    };

    if (idx === expect.length) {
      if (result < answer) {
        answer = result;
        return;
      };
    };

    for (let i = 0; i < 3; i++) {
      if (remains[i] !== 0) {
        remains[i] -= 1;
        req(idx + 1, [...remains], result + expect[idx][i]);
        remains[i] += 1;
      };
    };
  };

  req(0, [...picks], 0);

  
  return answer;
};

function makeCase(target) {
  let result = [0, 0, 0];
  const diaCount = target[0];
  const ironCount = target[1];
  const stoneCount = target[2];

  result[0] = diaCount + ironCount + stoneCount;
  result[1] = diaCount * 5 + ironCount + stoneCount;
  result[2] = diaCount * 25 + ironCount * 5 + stoneCount;

  return result;
};

console.log(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]));
console.log(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]));