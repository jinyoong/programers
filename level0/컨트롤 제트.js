function solution(s) {
  let answer = 0;
  let numbers = [];
  let sArray = s.split(" ");

  sArray.forEach(ele => {
    if (ele === "Z") {
      let lastNum = numbers.pop();
      answer -= lastNum ? lastNum : 0
    } else {
      answer += Number(ele);
      numbers.push(Number(ele));
    }
  })

  return answer;
}

console.log(solution("Z"))