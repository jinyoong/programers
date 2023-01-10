function solution(num_list, n) {
  const answer = [];
  let temp = [];
  let count = 0;

  num_list.map(element => {
    count += 1;
    temp.push(element);

    if (count === n) {
      answer.push(temp);
      temp = [];
      count = 0;
    }
  })

  return answer;
}