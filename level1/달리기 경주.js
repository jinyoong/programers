function solution(players, callings) {
  let playerObject = players.reduce((acc, cur, idx) => {
    acc[cur] = idx;
    return acc
  }, {});

  callings.forEach(calling => {
    const callingIdx = playerObject[calling];
    const targetIdx = callingIdx - 1;
    const target = players[targetIdx];

    players[targetIdx] = calling;
    players[callingIdx] = target;

    playerObject[calling] = targetIdx;
    playerObject[target] = callingIdx;
  });

  return players;
};

console.log(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]));