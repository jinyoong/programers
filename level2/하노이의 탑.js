function solution(n) {
  let answer = [[]];
  let temp = [[1, 3]];
  let count = 1;
  const firstHalf = [0, 1, 3, 2];
  const secondHalf = [0, 2, 1, 3];

  while (count < n) {
    answer = [];

    for (let element of temp) {
      let [start, end] = [...element];
      answer.push([firstHalf[start], firstHalf[end]]);
    };

    answer.push([1, 3]);

    for (let element of temp) {
      let [start, end] = [...element];
      answer.push([secondHalf[start], secondHalf[end]])
    };

    temp = [...answer];
    count += 1;
  }

  return answer;
}

/* 
n = 1인 경우
1 - 3

n = 2인 경우
1 - 2
1 - 3
2 - 3

n = 3인 경우
3개의 원판을 3번으로 옮기기 위해선, 3번 원판이 3번으로 가야 한다
즉, n - 1개의 원판을 3번이 아닌 2번으로 옮긴다고 생각하면 된다
1 - 3
1 - 2
3 - 2 -- 여기까지가 2개의 원판을 2번으로 옮긴 상태

1 - 3 -- 여기가 3번 원판을 3번으로 옮긴 상태

그럼 이제 2개의 원판을 2번에서 3번으로 옮기면 된다
2 - 1
2 - 3
1 - 3
*/

console.log(solution(3))