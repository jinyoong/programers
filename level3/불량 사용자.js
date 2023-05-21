function solution(userId, bannedId) {
  let answer = new Set();
  let visited = new Array(userId.length).fill(false);

  function req(bannedIdx, result) {
  
    if (bannedIdx === bannedId.length) {
      answer.add(result.sort().join(""));
      return;
    }

    const banned = bannedId[bannedIdx];
  
    for (let i = 0; i < userId.length; i++) {
      const user = userId[i];

      if (!visited[i] && isMatchUserAndBanned(user, banned)) {
        visited[i] = true;
        req(bannedIdx + 1, [...result, user]);
        visited[i] = false;
      }
    }
  }

  req(0, "");

  return answer.size;
}


function isMatchUserAndBanned(user, banned) {
  let result = true;

  if (user.length !== banned.length) {
    result = false;
    return result;
  }

  for (let i = 0; i < user.length; i++) {
    const bannedElement = banned[i];
    const userElement = user[i];

    if (!(bannedElement === "*" || bannedElement === userElement)) {
      result = false;
      break;
    }
  }

  return result;
}


console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]));
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]));
console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]));