function solution(before, after) {
  let answer = 1;
  const beforeObject = {};

  before.split("").map(element => {
    if (Object.hasOwn(beforeObject, element)) {
      beforeObject[element] += 1
    } else {
      beforeObject[element] = 1
    }
  })

  after.split("").map(element => {
    if (Object.hasOwn(beforeObject, element) && beforeObject[element] >= 1) {
      beforeObject[element] -= 1
      return
    }

    answer = 0;
    return
  })

  if (Object.values(beforeObject).filter(element => element !== 0).length !== 0) {
    answer = 0;
  }

  return answer;
}

function solution2(before, after) {
  answer = before.split("").sort().join("") === after.split("").sort().join("") ? 1 : 0
}

solution("olleh", "hello")