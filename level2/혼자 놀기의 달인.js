function solution(cards) {
  let answer = 1;
  let visited = new Array(cards.length + 1).fill(false);
  let numberArray = [];

  for (let start of cards) {

    const isVisited = visited[start];

    if (isVisited) continue;
    
    let current = start;
    let linkNumber = cards[current - 1]
    let count = 0;

    while (!visited[linkNumber]) {
      visited[linkNumber] = true;
      current = linkNumber;
      linkNumber = cards[current - 1];
      count += 1;
    };

    numberArray.push(count);
  };

  if (numberArray.length === 1) return 0;

  numberArray.sort((a, b) => b - a);
  answer = numberArray[0] * numberArray[1];

  return answer;
};

console.log(solution([8, 6, 3, 7, 2, 5, 1, 4]));
console.log(solution([2, 3, 4, 5, 6, 7, 8, 1]));
console.log(solution([1, 3, 4, 5, 6, 7, 8, 2]));
console.log(solution([2, 1]));
console.log(solution([2, 1, 4, 5, 6, 3, 8, 9, 10, 11, 7]))