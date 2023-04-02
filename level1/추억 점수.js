function solution(name, yearning, photo) {
  let answer = [];
  let nameScore = {};

  for (let i = 0; i < name.length; i++) {
    nameScore[name[i]] = yearning[i];
  };

  for (let photoElement of photo) {
    const result = photoElement.reduce((prev, curr) => {
      if (nameScore.hasOwnProperty(curr)) {
        return prev + nameScore[curr];
      };

      return prev;
    }, 0)

    answer.push(result);
  };

  return answer;
};

console.log(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))