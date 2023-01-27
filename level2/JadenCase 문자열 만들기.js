function solution(s) {
  const targets = s.split('');
  let answer = '';
  let before = ' ';

  targets.forEach(target => {
    if (target === ' ') {
      answer += target;
      before = ' ';
    }
    else if (before === ' ') {
      answer += target.toUpperCase();
      before = target;
      return;
    }
    else {
      answer += target.toLowerCase();
      before = target;
      return;
    }
  })

  return answer;
}