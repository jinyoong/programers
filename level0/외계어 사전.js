function solution(spell, dic) {
  var answer = 2;
  const sortedSpell = spell.sort().join("");

  for (let word of dic) {
    const sortedWord = word.split("").sort().join("");

    if (isInDic(sortedSpell, sortedWord)) {
      answer = 1
      break
    }
  }

  return answer;
}

function isInDic(spell, word) {
  if (word === spell) return true;
  return false;
}

solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])