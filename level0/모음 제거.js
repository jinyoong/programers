function solution(my_string) {
  var answer = '';
  const check = /[aeuio]/gi

  answer = my_string.replace(check, "");

  return answer;
}