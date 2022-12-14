function solution(array, height) {
  var answer = 0;

  for (let i = 0; i < array.length; i++) {
    if (array[i] > height) {
      answer += 1
    }
  }

  return answer;
}

function solution2(array, height) {
  var answer = array.filter((element) => element > height);
  return answer.length;
}