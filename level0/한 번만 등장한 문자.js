function solution(s) {
  const answer = [];
  let words = {};

  for (let i = 0; i < s.length; i++) {
    const word = s[i];

    if (Object.hasOwn(words, word)) {
      words[word] += 1;
      continue;
    };

    words[word] = 1;
  };

  for (const [key, value] of Object.entries(words)) {
    if (value === 1) {
      answer.push(key);
    };
  };

  return answer.sort().join("");
}

function solution2(s) {
  const answer = [];

  for (let word of s) {
    if (s.indexOf(word) === s.lastIndexOf(word)) {
      answer.push(word);
    };
  };

  return answer.sort().joint("");
}