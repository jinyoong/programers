function solution(quiz) {
  var answer = [];

  quiz.forEach((ele) => {
    let expression = ele.split(" ");
    let num1 = Number(expression[0]);
    let num2 = Number(expression[2]);
    let operator = expression[1];
    let num3 = Number(expression[4]);
    let result;

    if (operator === "+") {
      result = num1 + num2
    } else {
      result = num1 - num2
    }

    if (result != num3) {
      answer.push("X")
    } else {
      answer.push("O")
    }
  })

  return answer;
}