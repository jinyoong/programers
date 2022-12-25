function solution(price, money, count) {
  var answer = -1;
  let totalPrice = 0;

  if (count % 2 === 1) {
    totalPrice = price * (count + 1) * parseInt(count / 2) + parseInt(price * (count + 1) / 2)
  } else {
    totalPrice = price * (count + 1) * parseInt(count / 2)
  }

  answer = totalPrice - money > 0 ? totalPrice - money : 0 

  return answer;
}

console.log(solution(3, 20, 1))