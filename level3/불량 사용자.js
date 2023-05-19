function solution(userId, bannedId) {
  let answer = 0;
  let trie = new Trie(false);
  let words = [];

  userId.forEach(user => {
    let target = trie.node;

    for (let i = 0; i < user.length; i++) {
      const current = user[i];
      const isEnd = i === user.length - 1 ? true : false;

      if (trie.checkNodeNotInTarget(target, current)) {
        trie.addNode(target, current, isEnd);
      } 
      
      target = trie.getNextTarget(target, current);
    }
  })

  bannedId.forEach(banned => {
    let result = [];

    checkWord(banned, 0, trie.node, "", result);
    words.push(result);
  })

  let possibleSet = new Set();
  let subSet = new Set();

  calculateAnswer(words, 0, subSet, possibleSet);

  answer = possibleSet.size;
  
  return answer;
}

function checkWord(word, idx, subTarget, user, subResult) {
  const current = word[idx];

  if (idx === word.length) {
    if (subTarget["isEnd"] === true) {
      subResult.push(user);
    }

    return;
  }

  if (current === "*") {
    const keys = Object.keys(subTarget);
    
    keys.forEach(key => {
      if (key !== "isEnd") {
        checkWord(word, idx + 1, subTarget[key], user + key, subResult);
      }
    })
  } else {
    if (subTarget.hasOwnProperty(current)) {
      checkWord(word, idx + 1, subTarget[current], user + current, subResult);
    }
  }
}

function calculateAnswer(possibleWords, idx, result, targetSet) { 

  if (idx === possibleWords.length) {
    targetSet.add([...result].sort().join(""));
    return;
  }

  possibleWords[idx].forEach((possibleWord) => {
    if (result.has(possibleWord)) {
      return;
    }

    let newResult = new Set([...result]);
    newResult.add(possibleWord);

    calculateAnswer(possibleWords, idx + 1, newResult, targetSet);
  })
}

class Trie {
  constructor(isEnd) {
    this.node = { 
      isEnd
    }
  }

  addNode(target, current, isEnd) {
    const newNode = new Trie(isEnd);
    target[current] = newNode.node
  }

  checkNodeNotInTarget(target, current) {
    if (target.hasOwnProperty(current)) {
      return false;
    } else {
      return true;
    }
  }

  getNextTarget(target, current) {
    return target[current];
  }
}


console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]));
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]));
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]));