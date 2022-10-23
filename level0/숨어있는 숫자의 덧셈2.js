function solution(my_string) {
  let answer = 0;
  let number = 0;

  for (let i = 0; i < my_string.length; i++) {
    if (isNaN(my_string[i])) {
      if (number > 0) {
        answer += number
        number = 0
      }
    } else {
      number = number * 10 + Number(my_string[i])
    }
  }

  if (number > 0) {
    answer += number
  }

  return answer;
}