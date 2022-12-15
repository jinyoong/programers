function solution(k, score) {
  var answer = [];
  const scoreArray = new Array();

  score.map((element) => {

    if (scoreArray.length < k) {
      scoreArray.push(element);
    } else if (scoreArray[k - 1] < element) {
      scoreArray[k - 1] = element
    }

    scoreArray.sort((a, b) => b - a)
    answer.push(scoreArray[scoreArray.length - 1])

  })

  return answer;
}

console.log(solution(3, [10, 100, 20, 150, 1, 100, 200]))
console.log(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))