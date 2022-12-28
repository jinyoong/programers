function solution(num_list) {
  const answer = [0, 0];
  num_list.forEach(number => {
    if (number % 2 === 1) {
      answer[1] += 1
    } else {
      answer[0] += 1
    }
  })
  return answer;
}