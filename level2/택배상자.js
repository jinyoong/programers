function solution(order) {
  let answer = 0;
  let idx = 0;
  let box = 1;
  const subContainer = [];
  

  while (idx < order.length) {
    const requireBox = order[idx];

    if (box === requireBox) {
      idx += 1
      box += 1;
      answer += 1;
      continue;
    };

    if (subContainer[0] === requireBox) {
      idx += 1
      answer += 1;
      subContainer.shift();
      continue;
    };

    if (box > order.length && subContainer[0] !== requireBox) break;

    subContainer.unshift(box);
    box += 1;
  }

  return answer;
}

function solution2(order) {
  let answer = 0;
  const mainContainer = new Array(order.length).fill(0).map((valuen, index) => index + 1)
  const subContainer = new Array(order.length).fill(0);
  let subContainerIdx = 0;
  let mainIdx = 0;
  let idx = 0;

  while (idx < order.length && subContainerIdx < order.length) {
    const requireBox = order[idx];
    const mainBox = mainContainer[mainIdx];
    const subBox = subContainer[subContainerIdx];
    console.log(requireBox, mainBox, subBox)

    if (requireBox === mainBox) {
      mainIdx += 1;
      idx += 1;
      answer += 1;
      continue;
    };

    if (requireBox === subBox) {
      subContainerIdx -= subContainerIdx >= 1 ? 1 : 0;
      idx += 1;
      answer += 1;
      continue;
    }

    mainIdx += 1;
    subContainerIdx += 1;
    subContainer[subContainerIdx] = mainBox;
  }

  return answer;
}

console.log(solution2([4, 3, 1, 2, 5]))
console.log(solution([5, 4, 3, 2, 1]))