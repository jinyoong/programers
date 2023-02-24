function solution(keymap, targets) {
  let alpha = new Object();
  let answer = [];

  keymap.forEach(keyElement => {
    keyElement.split('').forEach((element, index) => {
      if (alpha.hasOwnProperty(element)) {
        if (alpha[element] > index + 1) {
          alpha[element] = index + 1;
        };
      } else {
        alpha[element] = index + 1;
      };
    });
  });

  targets.forEach(target => {
    let result = 0;
    
    for (let i = 0; i < target.length; i++) {
      const element = target[i];

      if (alpha[element] === undefined) {
        result = -1;
        break;
      } else {
        result += alpha[element];
      };
    };

    answer.push(result);
  });

  return answer;
};

console.log(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]));