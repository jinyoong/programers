function solution(begin, target, words) {
  let answer;
  let startSet = new Set();
  let queue = [[begin, 0, startSet]];
  let idx = 0;

  if (!words.includes(target)) {
    answer = 0;
    return answer;
  };

  while (idx < queue.length) {
    const current = queue[idx][0];
    const count = queue[idx][1];
    const visited = new Set(queue[idx][2]);
    idx += 1;

    if (current === target) {
      answer = count;
      break;
    };

    for (let i = 0; i < words.length; i++) {
      if (visited.has(i)) {
        continue;
      };

      const targetWord = words[i];
      let diffCount = 0;

      for (let j = 0; j < targetWord.length; j++) {
        if (targetWord[j] !== current[j]) {
          diffCount += 1;
        };

        if (diffCount > 1) {
          break;
        };
      };

      if (diffCount === 1) {
        queue.push([targetWord, count + 1, visited.add(i)]);
      };
    };
  };

  return answer;
};

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));