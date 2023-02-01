function solution(s){
  let answer = true;
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const element = s[i];
    if (element === '(') {
      stack.push(element)
      continue;
    }

    const lastElement = stack.pop();
    if (lastElement === undefined || lastElement !== '(') return false;
  }

  if (stack.length !== 0) answer = false;

  return answer;
}