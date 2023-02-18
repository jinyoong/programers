function solution(cards1, cards2, goal) {
  let answer = 'Yes';
  let card1Idx = 0;
  let card2Idx = 0;

  for (let goalIdx = 0; goalIdx < goal.length; goalIdx++) {
    const cards1Word = cards1[card1Idx];
    const cards2Word = cards2[card2Idx];
    const goalWord = goal[goalIdx];

    if (goalWord === cards1Word) {
      card1Idx += 1;
    } else if (goalWord === cards2Word) {
      card2Idx += 1;
    } else {
      answer = 'No';
      break;
    };
  };

  return answer;
};

console.log(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]));
console.log(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]));