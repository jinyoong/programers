function solution(ingredient) {
  var answer = 0;
  const sequence = [1, 3, 2, 1];
  const stack = [];

  ingredient.map((element, idx) => {
    stack.push(element);

    if (idx < 3) return;

    if (element !== 1) return;

    let isCorrect = true;
    for (let i = 0; i < 4; i++) {
      const idx = stack.length - i - 1;
      
      if (stack[idx] !== sequence[i]) {
        isCorrect = false;
        break;
      }
    }
    
    if (!isCorrect) return;
    
    for (let i = 0; i < 4; i++) {
      stack.pop();
    }
    answer += 1

  })

  return answer;
}

console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]));
console.log(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]));