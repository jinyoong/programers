function gcd(x, y) {
  let big;
  let small;

  if (x > y) {
    big = x; small = y;
  } else {
    big = y; small = x;
  }

  while (small != 0) {
    let new_big = small
    let new_small = big % small
    small = new_small
    big = new_big
  }

  return big
}

function lcm(x, y) {
  let gcdNum = gcd(x, y);
  return parseInt(x * y / gcdNum)
}

function solution(denum1, num1, denum2, num2) {
  var answer = [];

  let newNum = lcm(num1, num2);
  let newDenum1 = denum1 * parseInt(newNum / num1)
  let newDenum2 = denum2 * parseInt(newNum / num2)
  let newDenum = newDenum1 + newDenum2
  let totalGcd = gcd(newDenum, newNum)
  answer[0] = parseInt(newDenum / totalGcd)
  answer[1] = parseInt(newNum / totalGcd)

  return answer;
}

solution(1, 2, 3, 4);