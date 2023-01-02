function solution(my_string) {
  let answer = '';

  my_string.split("").map(element => {
    const upperElement = element.toUpperCase();

    if (upperElement === element) {
      answer += element.toLowerCase();
      return
    }

    answer += upperElement;
  })

  return answer;
}