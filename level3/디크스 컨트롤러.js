function solution(jobs) {
  let answer = 0;
  let currentTime = 0;
  let minHeap = new MinHeap();
  let pushArray = [];

  for (let job of jobs) {
    const need = job[1];
    const start = job[0];
    minHeap.heapPush([need, start]);
  }

  while (minHeap.size() > 0) {
    const [time, start] = minHeap.heapPop();
    let target = [time, start];

    while (minHeap.size() > 0) {
      const [otherTime, otherStart] = minHeap.heapPop();
      const expectEndTime = calulateEndTime(currentTime, otherTime, otherStart);

      if (start >= expectEndTime) {
        minHeap.heapPush(target);
        target = [otherTime, otherStart];
        break;
      }

      pushArray.push([otherTime, otherStart]);
    }

    while (pushArray.length > 0) {
      minHeap.heapPush(pushArray.pop())
    }

    answer += totalTime(currentTime, target[0], target[1]);
    currentTime = calulateEndTime(currentTime, target[0], target[1]);
  }

  return parseInt(answer / jobs.length);
}

function calulateEndTime(currentTime, time, start) {
  let result = 0;

  if (currentTime <= start) {
    result = start + time;
  } else {
    result = currentTime + time;
  }

  return result;
}

function totalTime(currentTime, time, start) {
  let result = 0;

  if (currentTime <= start) {
    result = time;
  } else {
    result = time + currentTime - start;
  }

  return result;
}

class MinHeap {
  constructor() {
    this.heap = [];
  }

  heapPush([x, start]) {
    this.heap.push([x, start]);
    let childIdx = this.heap.length - 1;
    let child = this.heap[childIdx];
    
    while (childIdx >= 1) {
      let parentIdx = parseInt(childIdx / 2);
      let parent = this.heap[parentIdx];

      if (parent[0] > child[0]) {
        this.heap[parentIdx] = child;
        this.heap[childIdx] = parent;

        childIdx = parentIdx;
      } else {
        break;
      }
    }
  }

  heapPop() {
    const heapLength = this.heap.length;

    if (heapLength === 0) {
      return null
    }

    let result = this.heap[0];
    this.heap[0] = this.heap[heapLength - 1];
    this.heap.pop();
    let lastIdx = heapLength - 2;
    let parentIdx = 0;
    let parent = this.heap[parentIdx];
    let childIdx = 2 * parentIdx + 1;
    let child = this.heap[childIdx];

    while (childIdx <= lastIdx) {
      if (childIdx + 1 <= lastIdx) {
        const rightChild = this.heap[childIdx + 1];

        if (child[0] > rightChild[0]) {
          child = rightChild;
          childIdx += 1;
        }
      }

      if (parent[0] > child[0]) {
        this.heap[parentIdx] = child;
        this.heap[childIdx] = parent;

        parentIdx = childIdx
        childIdx = 2 * parentIdx;
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

console.log(solution([[0, 3], [1, 9], [2, 6]]));
console.log(solution([[0, 3], [10, 1]])); // 2
console.log(solution([[7, 8], [3, 5], [9, 6]])); // 9
console.log(solution([[1, 4], [7, 9], [1000, 3]])); // 5
console.log(solution([[0, 1], [2, 2], [2, 3]])) // 2