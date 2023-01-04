function solution(my_string) {
  let answer = [];

  my_string.split("").filter(element => !isNaN(element)).sort((a, b) => b - a).map(element => {
    answer.push(Number(element))
  })


  return answer;
}