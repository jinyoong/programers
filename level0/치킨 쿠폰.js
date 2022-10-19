function solution(chicken) {
  var answer = 0;

  while (chicken >= 10) {
    let service = parseInt(chicken / 10);
    let remain = chicken % 10;
    answer += service
    chicken = service + remain
  }

  return answer;
}