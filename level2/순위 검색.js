function solution(info, query) {
  let answer = [];
  const infoObject = {};

  info.forEach(infoElement => {
    const infoArray = infoElement.split(" ");
    const infoKey = infoArray.slice(0, 4).join(":");
    const infoValue = Number(infoArray[4]);
    
    if (infoObject[infoKey]) {
      infoObject[infoKey].push(infoValue);
    } else {
      infoObject[infoKey] = [infoValue];
    };
  });

  for (let infoKey in infoObject) {
    const sortedInfoValue = infoObject[infoKey].sort((a, b) => a - b);
    infoObject[infoKey] = sortedInfoValue;
  };

  query.forEach(queryElement => {
    const queryArray = queryElement.replaceAll("and ", "").replaceAll("-", "").split(" ");
    const queryKey = queryArray.slice(0, 4);
    const queryValue = Number(queryArray[4]);
    let result = 0;

    for (let infoKey in infoObject) {
      const infoValue = infoObject[infoKey]
      
      if (queryKey.every(element => infoKey.includes(element))) {
        result += infoValue.length - search(infoValue, queryValue);
      };
    };
    answer.push(result);
  });

  return answer;
};

function search(numbers, target) {
  let start = 0;
  let end = numbers.length - 1;
  let middle;

  while (start <= end) {
    middle = parseInt((start + end) / 2);

    if (numbers[middle] < target) {
      start = middle + 1;

      if (numbers[middle + 1] >= target) {
        middle += 1;
        break;
      };
    } else {
      end = middle - 1;

      if (numbers[middle - 1] < target) {
        break;
      };
    };
  };

  if (numbers[middle] < target) {
    return middle + 1;
  };

  return middle;
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