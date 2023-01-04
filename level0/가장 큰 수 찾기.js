function solution(array) {
  const answer = [0, 0];

  array.forEach((element, index) => {
    if (element > answer[0]) {
      answer[0] = element
      answer[1] = index
    }
  })

  return answer;
}