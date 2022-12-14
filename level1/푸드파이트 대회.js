function solution(food) {
  var answer = '';
  const result = new Array(food.length - 1).fill(0)
  
  food.slice(1).forEach((element, idx) => {
    result[idx] += parseInt(element / 2)

  })

  let side = ""
  for (let i = 0; i < result.length; i++) {
    side += String(i + 1).repeat(result[i])
  }
  
  answer = side + "0" + side.split("").reverse().join("")
  return answer;
}

console.log(solution([1, 3, 4, 6]))