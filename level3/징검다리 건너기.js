function solution(stones, k) {
  let answer = 0;
  let section = new Heap();

  for (let i = 0; i < stones.length; i++) {
    const stone = stones[i];
    section.heapPush(stone);
  };

  return answer;
};

class Heap {
  constructor() {
    this.heap = [0];
  };

  heapPush(x) {
    this.heap.push(x);
    let childIdx = this.heap.length - 1;
    let childNum = this.heap[childIdx];

    while(childIdx > 1) {
      const parentIdx = parseInt(childIdx / 2);
      const parentNum = this.heap[parentIdx];

      if (parentNum < childNum) {
        this.heap[childIdx] = parentNum;
        this.heap[parentIdx] = childNum;
        childIdx = parentIdx;
        childNum = parentNum;
      } else {
        break;
      };
    };
  };

  heapPop() {
    const result = this.heap[1];
    let lastIdx = this.heap.length - 1;
    let parentIdx = 1;

    this.heap[1] = this.heap[lastIdx];
    this.heap.pop();
    lastIdx -= 1;

    while(parentIdx * 2 <= lastIdx) {
      const parent = this.heap[parentIdx];
      let childIdx = parentIdx * 2;
      let child = this.heap[childIdx];
      
      if (2 * parentIdx + 1 <= lastIdx) {
        const rightChild = this.heap[2 * parentIdx + 1];

        if (child < rightChild) {
          child = rightChild;
          childIdx += 1;
        };
      };

      if (parent < child) {
        this.heap[parentIdx] = child;
        this.heap[childIdx] = parent;
        parentIdx = childIdx;
      };
    };

    return result
  };
};

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
console.log(solution([3, 1, 2, 1], 3));