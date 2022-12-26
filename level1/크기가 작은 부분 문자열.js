function solution(t, p) {
  var answer = 0;
  let temp = "";
  const pLength = p.length;

  t.split("").map(element => {
    temp += element;

    if (temp.length === pLength) {
      if (parseInt(temp) <= parseInt(p)) {
        answer += 1
      }

      temp = temp.substring(1);
    }
  });

  return answer;
}

console.log(solution("3141592", "271"))
console.log(solution("10203", "15"))