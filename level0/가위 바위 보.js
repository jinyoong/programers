function solution(rsp) {
  let answer = '';

  const win = {"2": "0", "0": "5", "5": "2"};

  rsp.split("").map(element => {
    answer += win[element]
  })

  return answer;
}