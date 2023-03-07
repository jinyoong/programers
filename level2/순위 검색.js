function solution(info, query) {
  var answer = [];
  const sortedInfo = info.map(element => element.split(" ")).sort((a, b) => Number(a[4]) - Number(b[4]))

  query.forEach(element => {
    const targetArray = element.replaceAll("and ", "").split(" ");
    const targetScore = Number(targetArray[4]);
    let start = 0;
    let end = sortedInfo.length;
    let middle;
    let middleScore;
    
    while (start < end) {
      middle = parseInt((start + end) / 2);
      middleScore = Number(sortedInfo[middle][4]);

      if (middleScore < targetScore) {
        start = middle + 1;

        if (sortedInfo[middle + 1][4] >= targetScore) {
          middle += 1;
          break;
        };
      } else {
        end = middle - 1;

        if (sortedInfo[middle - 1][4] < targetScore) {
          break;
        };
      };
    };

    let result = 0;

    console.log(sortedInfo)
    console.log(middle)

    for (let i = middle; i < sortedInfo.length; i++) {
      let isBreak = false;

      for (let j = 0; j < 4; j++) {
        const infoElement = sortedInfo[i][j];
        const queryElement = targetArray[j];

        console.log("지원자의 역량 : ", infoElement);
        console.log("요구 역량 : ", queryElement);

        if (queryElement === "-") {
          continue;
        } else {
          if (queryElement !== infoElement) {
            isBreak = true;
            break;
          };
        };
      };

      if (!isBreak) {
        result += 1;
      };
    };

    console.log(result);
    answer.push(result);
  });

  return answer;
};

console.log(
  solution(
  [
    "java backend junior pizza 150", 
    "python frontend senior chicken 210", 
    "python frontend senior chicken 150", 
    "cpp backend senior pizza 260", 
    "java backend junior chicken 80", 
    "python backend senior chicken 50"
  ], 
  [
    "java and backend and junior and pizza 100", 
    "python and frontend and senior and chicken 200", 
    "cpp and - and senior and pizza 250", 
    "- and backend and senior and - 150", 
    "- and - and - and chicken 100", 
    "- and - and - and - 150"
  ]))