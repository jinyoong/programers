function solution(data, col, row_begin, row_end) {
  let answer = 0;
  const sortedData = data.sort((a, b) => {
    if (a[col - 1] > b[col - 1]) return 1;

    if (a[col - 1] < b[col - 1]) return -1;

    if (a[0] > b[0]) return -1;
    
    if (a[0] < b[0]) return 1;
  });

  const modData = [];


  sortedData.slice(row_begin - 1, row_end).forEach((element, index) => {
    let modResult = 0;
    element.forEach(data => {
      modResult += data % (row_begin + index);
    });
    modData.push(modResult);
  });

  let count = 0;
  
  while (modData.some(element => element !== 0)) {
    let result = -1;

    modData.forEach((element, index) => {
      if (index === 0) result = element % 2;
      else {
        if (result === element % 2) result = 0;
        else result = 1;
      };
      modData[index] = parseInt(element / 2);
    });

    if (result === 1) answer += (2 ** count);

    count += 1;
  };
  return answer;
}

console.log(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3));