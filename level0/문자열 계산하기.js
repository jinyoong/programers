function solution(my_string) {
  let stringArray = my_string.split(" ")
  let answer = Number(stringArray[0]);

  for (let i = 2; i < stringArray.length; i += 2) {

    if (stringArray[i - 1] === "+") {
      answer += Number(stringArray[i])
    } else {
      answer -= Number(stringArray[i])
    }
  }

  return answer;
}

console.log(solution("3 + 4"))