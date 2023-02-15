function solution(k, ranges) {
  let answer = [];
  let areas = [0];
  let number = k;
  let nextNumber = 0;
  let idx = 0;

  while (number !== 1) {
    
    if (number % 2 === 0) {
      nextNumber = parseInt(number / 2);
    } else {
      nextNumber = number * 3 + 1;
    };

    const area = (nextNumber + number) / 2
    areas.push(area + areas[idx]);
    idx += 1;
    number = nextNumber;
  };

  ranges.forEach(range => {
    const start = range[0];
    const end = areas.length - 1 + range[1];
    let result;

    if (start <= end) {
      result = areas[end] - areas[start];
    } else {
      result = -1;
    }

    answer.push(result);
  });

  return answer;
};

console.log(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]));