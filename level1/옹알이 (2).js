function solution(babbling) {
  var answer = 0;
  const words = ["aya", "ye", "woo", "ma"];
  babbling.map((element) => {

    if (element.length == 1) {
      return;
    };
    
    let target = "";
    let before = "";
    for (let i = 0; i < element.length; i++) {

      target += element[i];
      if (words.includes(target) && before != target) {
        before = target
        target = "";
      } else if (target.length == 4) {
        return
      }

    }

    if (target.length >= 1) {
      return
    }

    answer += 1

  })

  return answer;
}

console.log(solution(["aya", "yee", "u", "maa"]))
console.log(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
console.log(solution(["yemawoo"]))

function solution2(babbling) {
  const regexp1 = /(aya|ye|woo|ma)\1+/;
  const regexp2 = /^(aya|ye|woo|ma)+$/;

  return babbling.reduce((ans, word) => (
    !regexp1.test(word) && regexp2.test(word) ? ++ans : ans
  ), 0);
}