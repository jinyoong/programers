function solution(x, y, n) {
  const queue = [x];
  const visited = new Array(y - x + 1).fill(0);
  let idx = 0;
  let length = 1;

  while (idx < length) {
    const current = queue[idx];
    const count = visited[current - x];
    idx += 1;
    
    if (current === y) return count;

    let nextNumber = 0;

    for (const nextNumber of [current * 3, current * 2, current + n]) {

      if (visited[nextNumber - x] !== 0) continue;

      if (nextNumber > y) continue;

      queue.push(nextNumber);
      visited[nextNumber - x] = count + 1;
      length += 1
    };
  };

  return -1;
};

console.log(solution(10, 40, 5));
console.log(solution(10, 40, 30));
console.log(solution(2, 5, 4));