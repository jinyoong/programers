function solution(my_str, n) {
  let answer = [];

  for (let i = 0; i < my_str.length; i += n) {
    const start = i
    const end = i + n

    answer.push(my_str.substring(start, end))
  }

  return answer;
}