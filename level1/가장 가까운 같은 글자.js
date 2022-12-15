function solution(s) {
  var answer = [];
  const alpha = new Object();

  for (let i = 0; i < s.length; i++) {
    const target = s[i];

    if (Object.hasOwn(alpha, target)) {
      answer.push(i - alpha[target]);
    } else {
      answer.push(-1);
    }
    
    alpha[target] = i;
  };

  return answer;
}

console.log(solution("banana"))
console.log(solution("foobar"))