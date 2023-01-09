function solution(my_string) {
  var answer = '';
  const alpha = new Set();

  my_string.split("").map(element => {
    if (alpha.has(element)) {
      return
    }

    answer += element
    alpha.add(element)
  })

  return answer;
}