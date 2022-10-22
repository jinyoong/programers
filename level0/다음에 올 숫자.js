function solution(common) {
  var answer = 0;

  let diff1 = common[1] - common[0]
  let diff2 = common[2] - common[1]
  console.log(diff1, diff2)

  if (diff1 === diff2) {
    answer = common.pop() + diff1
  } else {
    answer = common.pop() * common[1] / common[0]
  }

  return answer;
}

console.log(solution([1, 2, 3, 4]))