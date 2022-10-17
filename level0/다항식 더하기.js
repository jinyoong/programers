function solution(polynomial) {
  var answer = '';
  let polynomialArray = polynomial.split(" + ")
  let number = new Array(2).fill(0);

  polynomialArray.forEach(element => {
    if (element.indexOf("x") != -1) {
      let point = element.replace("x", "")
      number[0] += point ? Number(point) : 1
    } else {
      number[1] += Number(element)
    }
  })

  if (number[0] != 0) {
    
    if (number[0] == 1) {
      answer += "x"
    } else{
      answer += `${number[0]}x`
    }
  }

  if (number[1] != 0) {
    
    if (number[0] != 0) {
      answer += " + "
    }

    answer += `${number[1]}`
  }

  return answer;
}