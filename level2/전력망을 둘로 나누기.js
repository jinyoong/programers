function countNode(node, subTree) {
  const queue = [node];
  const visited = new Set();
  let idx = 0;
  let length = 1;

  visited.add(node);

  while (idx < length) {
    const current = queue[idx];
    idx += 1;

    for (let nextNode = 0; nextNode < subTree.length; nextNode++) {
      const value = subTree[current][nextNode];

      if (value === 0) continue;

      if (visited.has(nextNode)) continue;

      queue.push(nextNode);
      visited.add(nextNode);
      length += 1;
    }
  }

  return queue.length;
}

function solution(n, wires) {
  let answer = 100;
  const tree = new Array(n + 1).fill(0).map(() => new Array(n + 1).fill(0))

  for (let wire of wires) {
    const [n1, n2] = wire;
    tree[n1][n2] = 1;
    tree[n2][n1] = 1;
  }

  for (let wire of wires) {
    const [n1, n2] = wire;
    tree[n1][n2] = 0;
    tree[n2][n1] = 0;

    const n1Count = countNode(n1, tree);
    const n2Count = countNode(n2, tree);
    const diff = Math.abs(n1Count - n2Count);

    if (diff < answer) answer = diff;

    tree[n1][n2] = 1;
    tree[n2][n1] = 1;
  }

  return answer;
}

console.log(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
console.log(solution(2, [[1, 2]]))
console.log(solution(3, [[1, 2], [2, 3]]))