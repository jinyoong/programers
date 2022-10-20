function solution(score) {
  let answer = new Array(score.length).fill(0);
  let totalScore = new Array(201).fill(0).map(() => new Array());

  for (let i = 0; i < score.length; i++) {
    let english = score[i][0]
    let math = score[i][1]
    console.log(english + math)
    totalScore[english + math].push(i)
  }

  console.log(totalScore)
  let rank = 1
  for (let i = 200; i >= 0; i--) {
    if (totalScore[i].length === 0) {
      continue
    } else {
      let count = 0;
      
      totalScore[i].forEach((idx) => {
        answer[idx] = rank
        count += 1
      })

      rank += count
    }
  }

  return answer;
}