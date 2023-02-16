class maxHeap {
  constructor() {
    this.heap = [0];
  };

  heapLength() {
    return this.heap.length;
  };

  heapPush(x) {
    this.heap.push(x);
    let idx = this.heap.length - 1;
    
    while (idx > 1) {
      const child = this.heap[idx];
      const parent = this.heap[parseInt(idx / 2)];

      if (parent < child) {
        this.heap[idx] = parent;
        this.heap[parseInt(idx / 2)] = child;
        idx = parseInt(idx / 2);
      } else {
        break;
      };
    };
  };

  heapPop() {
    
    if (this.heap.length === 2) {
      return this.heap.pop();
    } else if (this.heap.length === 1) {
      return -1;
    };

    const result = this.heap[1];
    this.heap[1] = this.heap.pop();
    let idx = 1;

    while (2 * idx < this.heap.length) {
      const parent = this.heap[idx];
      let targetChild;
      let targetIdx;

      if (2 * idx + 1 < this.heap.length) {
        const leftChild = this.heap[2 * idx];
        const rightChild = this.heap[2 * idx + 1];

        if (leftChild >= rightChild) {
          targetChild = leftChild;
          targetIdx = 2 * idx;
        } else {
          targetChild = rightChild;
          targetIdx = 2 * idx + 1;
        };
      } else {
        targetChild = this.heap[2 * idx];
        targetIdx = 2 * idx;
      };

      if (parent < targetChild) {
        this.heap[idx] = targetChild;
        this.heap[targetIdx] = parent;
        idx = targetIdx;
      } else {
        break;
      };
    };

    return result;
  }
};

function solution(n, k, enemy) {
  let answer = 0;

  if (enemy.reduce((prev, curr) => prev + curr) <= n) return enemy.length;

  if (enemy.length <= k) return enemy.length;

  let enemyHeap = new maxHeap();
  let sumOfEnemy = 0;
  let count = 0;

  for (let element of enemy) {
    sumOfEnemy += element;
    enemyHeap.heapPush(element);
    
    while (sumOfEnemy > n && enemyHeap.heapLength() >= 2 && count < k) {
      sumOfEnemy -= enemyHeap.heapPop();
      count += 1;
    };

    if (sumOfEnemy > n && count === k) break;

    answer += 1;
  };

  return answer;
};

console.log(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]));
console.log(solution(2, 1, [1, 1, 100, 1]));
console.log(`예상 : 5, 실제 : ${solution(7, 3, [5, 5, 5, 5, 2, 3 ,1])}`);
console.log(`예상 : 7, 실제 : ${solution(1, 6, [2, 2, 2, 2, 3, 3, 1])}`);
console.log(`예상 : 6, 실제 : ${solution(10, 1, [2, 2, 2, 2, 2, 10])}`);
console.log(`예상 : 5, 실제 : ${solution(10, 1, [2, 2, 2, 2, 10])}`);
console.log(solution(2, 2, [2, 2, 1, 1]));
console.log(`예상 : 5, 실제 : ${solution(4, 1, [1, 1, 100, 1, 1])}`);
console.log(solution(999999998, 1, [999999999, 1000000000]));
console.log(solution(10, 2, [3, 8, 2, 5, 5]))