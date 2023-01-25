function solution2(k, d) {
  /*
  구해야 하는 영역은 1사분면 위의 (0, 0)을 중심으로 하는 사분원의 영역이다
  그렇다면 (0, 0), (d, 0), (0, d)를 꼭지점으로 하는 삼각형 안에 들어가는 점들은 무조건 해당된다는 뜻이 된다
  이 때, 점은 k의 배수로 진행되니까 (0, 0), (d // k, 0), (0, d // k) 삼각형 내의 점들의 개수를 먼저 구해주면 된다
  */
  let answer = 0;
  const COUNT = parseInt(d / k) + 1;

  answer += (1 + COUNT) * COUNT / 2;

  for (let i = 1; i < COUNT; i++) {
    const maxPoint = Math.sqrt((d / k) ** 2 - i ** 2);
    const point = COUNT - i - 1;
    
    answer += parseInt(maxPoint - point)
  }

  return answer;
}

console.log(solution2(2, 4))
console.log(solution2(1, 5))
console.log(solution2(3, 8))
console.log(solution2(2, 2))
console.log(solution2(1, 1000000))