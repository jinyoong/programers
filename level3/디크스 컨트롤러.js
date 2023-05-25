function solution(jobs) {
  let answer = 0;
  let endTime = -1;
  let currentTime = 0;
  let count = 0;
  let minHeap = new MinHeap();

  // while (count < jobs.length) {

  //   for (let job of jobs) {
  //     const start = job[0];
  //     const time = job[1];

  //     if (endTime < start && start <= currentTime) {
  //       minHeap.heapPush([time, start]);
  //     }
  //   }

  //   if (minHeap.size() === 0) {
  //     currentTime += 1;
  //   } else {
  //     const target = minHeap.heapPop();
  //     const targetTime = target[0];
  //     const targetStart = target[1];
  //     console.log("타겟 : ", target)
  //     console.log(minHeap);
      
  //     currentTime += targetTime;
  //     answer += currentTime - targetStart;
  //     endTime = targetStart;
  //     count += 1;
  //   }
  // }

  for (let job of jobs) {
    minHeap.heapPush([job[1], job[0]])
  }

  console.log(minHeap.heap);

  for (let i = 0; i < jobs.length + 1; i++) {
    minHeap.heapPop();
    console.log(minHeap.heap);
  }

  console.log(answer);
  return parseInt(answer / jobs.length);
}

class MinHeap {
  constructor() {
    this.heap = [];
  }

  heapPush([x, start]) {
    this.heap.push([x, start]);
    let childIdx = this.heap.length - 1;
    
    while (childIdx >= 1) {
      const parentIdx = parseInt(childIdx / 2);
      const parent = this.heap[parentIdx];
      const child = this.heap[childIdx];

      if (parent[0] > child[0]) {
        this.heap[parentIdx] = [...child];
        this.heap[childIdx] = [...parent];

        childIdx = parentIdx;
      } else {
        break;
      }
    }
  }

  heapPop() {
    if (this.size() === 0) {
      return null
    }

    let result = [...this.heap[0]];
    let lastIdx = this.size() - 2;
    let parentIdx = 0;
    let childIdx = 2 * parentIdx + 1;
    this.heap[0] = [...this.heap[lastIdx + 1]];
    this.heap.pop();

    while (childIdx <= lastIdx) {
      let child = [...this.heap[childIdx]];
      if (childIdx + 1 <= lastIdx) {
        const rightChild = [...this.heap[childIdx + 1]];

        if (child[0] > rightChild[0]) {
          child = [...rightChild];
          childIdx += 1;
        }
      }

      let parent = [...this.heap[parentIdx]];

      if (parent[0] > child[0]) {
        this.heap[parentIdx] = [...child];
        this.heap[childIdx] = [...parent];

        parentIdx = childIdx
        childIdx = 2 * parentIdx + 1;
      } else {
        break;
      }
    }

    return result;
  }

  size() {
    return this.heap.length;
  }
}

// console.log(solution([[0, 3], [1, 9], [2, 6]]));
// console.log(solution([[0, 3], [10, 1]])); // 2
// console.log(solution([[7, 8], [3, 5], [9, 6]])); // 9
// console.log(solution([[1, 4], [7, 9], [1000, 3]])); // 5
// console.log(solution([[0, 1], [2, 2], [2, 3]])) // 2
// console.log(solution([[0, 3], [4, 4], [5, 3], [4, 1]]))
console.log(solution([[0,16],[0,14],[15,1],[13,13]]));
console.log(solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]]));