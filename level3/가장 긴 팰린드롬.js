function solution(s) {
  let answer = 1;

  for (let i = s.length; i > 1; i--) {
    for (let j = 0; j <= s.length - i; j++) {
      if (isPalindrome(s, i, j)) {
        answer = i;
        return answer;
      };
    };
  };

  return answer;
};

function isPalindrome(word, targetLength, start) {
  let result = true;

  for (i = 0; i < parseInt(targetLength / 2); i++) {
    if (word[start + i] !== word[start + targetLength - i - 1]) {
      result = false;
      break;
    };
  };

  return result;
};

console.log(solution("abcdcba"));
console.log(solution("abacde"));