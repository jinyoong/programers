function solution(stones, k) {
  let answer = 200000000;
  let section = new Heap();

  for (let i = 0; i < stones.length; i++) {
    const stone = stones[i];
    section.heapPush(stone, i);

    if (i >= k - 1) {
      while (section.heap[1][1] <= i - k) {
        section.heapPop();
      };

      answer = Math.min(answer, section.heap[1][0]);
    };
  };

  return answer;
};

class Heap {
  constructor() {
    this.heap = [[0, -1]];
  };

  heapPush(x, idx) {
    this.heap.push([x, idx]);
    let childIdx = this.heap.length - 1;
    let childValue = this.heap[childIdx][0];
    let childValueIdx = this.heap[childIdx][1];

    while(childIdx > 1) {
      const parentIdx = parseInt(childIdx / 2);
      const parentValue = this.heap[parentIdx][0];
      const parentValueIdx = this.heap[parentIdx][1];

      if (parentValue < childValue) {
        this.heap[childIdx] = [parentValue, parentValueIdx];
        this.heap[parentIdx] = [childValue, childValueIdx];
        childIdx = parentIdx;
        childValue = parentValue;
        childValueIdx = parentValueIdx;
      } else {
        break;
      };
    };
  };

  heapPop() {
    let lastIdx = this.heap.length - 1;
    let parentIdx = 1;

    this.heap[1] = [...this.heap[lastIdx]];
    this.heap.pop();
    lastIdx -= 1;

    while(parentIdx * 2 <= lastIdx) {
      const parentValue = this.heap[parentIdx][0];
      const parentValueIdx = this.heap[parentIdx][1];

      let childIdx = parentIdx * 2;
      let childValue = this.heap[childIdx][0];
      let childValueIdx = this.heap[childIdx][1];
      
      if (2 * parentIdx + 1 <= lastIdx) {
        const rightChild = this.heap[2 * parentIdx + 1];

        if (childValue < rightChild[0]) {
          childValue = rightChild[0];
          childValueIdx = rightChild[1];
          childIdx += 1;
        };
      };

      if (parentValue < childValue) {
        this.heap[parentIdx] = [childValue, childValueIdx];
        this.heap[childIdx] = [parentValue, parentValueIdx];
        parentIdx = childIdx;
      } else {
        break;
      };
    };
  };
};

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
console.log(solution([200, 100, 1, 50], 2));
console.log(solution([3, 1, 2, 1], 3));