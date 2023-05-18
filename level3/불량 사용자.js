function solution(userId, bannedId) {
  let answer = 0;
  let trie = new Trie();

  userId.forEach(user => {
    for (let i = 0; i < user.length; i++) {
      const word = user[i];
      const next = (i + 1) < user.length ? user[i + 1] : null;
      const isEnd = i === user.length - 1 ? true : false;

      if (trie.checkInTrie(word)) {
        const target = trie.getNodes(word);
        trie.addNode(target, next);
      } else {
        trie.makeNode(word, isEnd);
      }

    }
  })

  bannedId.forEach(banned => {
    for (let i = 0; i < banned.length; i++) {
      const word = banned[i];

      if (i === 0) {
        
      } else if (i === banned.length - 1) {
        
      } else {

      }
    }
  })
  
  console.log(trie.object);

  return answer;
}

class Trie {
  constructor() {
    this.object = new Object();
  }

  makeNode(head, isEnd) {
    this.object[head] = [isEnd];
  }

  checkInTrie(head) {
    if (this.object.hasOwnProperty(head)) {
      return true;
    } else {
      return false;
    };
  }

  getNodes(head) {
    let nodes = this.object[head];
    return nodes;
  }

  addNode(nodes, next) {
    if (next && !nodes.includes(next)) {
      nodes.push(next);
    }
  }
}


console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]));
// console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]));
// console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]));