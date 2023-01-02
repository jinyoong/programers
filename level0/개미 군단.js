function solution(hp) {
  let answer = 0;

  [5, 3, 1].map(element => {
    
    answer += parseInt(hp / element);
    hp %= element

  })

  return answer;
}