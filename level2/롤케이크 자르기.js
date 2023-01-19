function solution(topping) {
  const maxTopping = Math.max(...topping);
  const brotherTopping = new Array(maxTopping + 1).fill(0);
  const myTopping = new Array(maxTopping + 1).fill(0);
  let answer = 0;
  let brotherToppingCount = 0;
  let myToppingCount = 0;

  for (let element of topping) {
    if (brotherTopping[element] === 0) brotherToppingCount += 1
    brotherTopping[element] += 1
  }

  for (let element of topping) {
    if (myTopping[element] === 0) myToppingCount += 1
    myTopping[element] += 1

    if (brotherTopping[element] === 1) brotherToppingCount -= 1
    brotherTopping[element] -= 1

    if (myToppingCount === brotherToppingCount) answer += 1
  }

  return answer;
}

function solution2(topping) {
  const brotherTopping = new Object();
  const myTopping = new Object();
  let answer = 0;
  let brotherToppingCount = 0;
  let myToppingCount = 0;

  for (let element of topping) {
    if (!Object.hasOwn(brotherTopping, element)) {
      brotherToppingCount += 1
      brotherTopping[element] = 1
    } else {
      brotherTopping[element] += 1
    }
  }

  for (let element of topping) {
    if (!Object.hasOwn(myTopping, element)) {
      myToppingCount += 1
      myTopping[element] = 1
    } else {
      myTopping[element] += 1
    }

    if (brotherTopping[element] === 1) brotherToppingCount -= 1
    brotherTopping[element] -= 1

    if (myToppingCount === brotherToppingCount) answer += 1
  }

  return answer;
}

console.log(solution2([1, 2, 1, 3, 1, 4, 1, 2]))
console.log(solution2([1, 2, 3, 1, 4]))