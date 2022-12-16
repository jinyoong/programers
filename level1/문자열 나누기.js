function solution(s) {
  var answer = 0;
  let start = s[0];
  let equalCount = 0;
  let differentCount = 0;

  s.split("").map((element, idx) => {

    if (element === start) {
      equalCount += 1;
    } else {
      differentCount += 1;
    };

    if (equalCount === differentCount) {
      answer += 1
      equalCount = 0;
      differentCount = 0;

      if (idx == s.length - 1) {
        return
      }

      start = s[idx + 1]
    }
  })

  if (equalCount >= 1 || differentCount >= 1) {
    answer += 1
  }

  return answer;
}

console.log(solution("banana"))
console.log(solution("abracadabra"))
console.log(solution("aaabbaccccabba"))