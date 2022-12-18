function solution(elements) {
  const numbers = new Set()
  const MAX = elements.reduce((prev, curr) => prev + curr);
  numbers.add(MAX);

  elements.map((element, idx) => {
    let temp = 0;

    for (let i = 0; i <= parseInt(elements.length / 2); i++) {
      temp += elements[(idx + i) % elements.length]
      numbers.add(temp)
      numbers.add(MAX - temp)
    }
  })

  return numbers.size;
}

console.log(solution([7, 9, 1, 1, 4]));