function solution(operations) {
  let answer = [];
  let maxHeap = new Heap();
  let minHeap = new Heap();
  let needPopMax = new Map();
  let needPopMin = new Map();

  operations.forEach(operation => {
    const [order, number] = seperate(operation);
    
    if (order === 'I') {
      maxHeap.heapPush(number);
      minHeap.heapPush(-number);
      return;
    };

    if (number === 1) {
      popFromHeap(maxHeap, needPopMax);

      const popResult = maxHeap.heapPop();

      addToMap(-popResult, needPopMin)
    } else {
      popFromHeap(minHeap, needPopMin);

      const popResult = minHeap.heapPop();

      addToMap(-popResult, needPopMax);
    };

  });
  
  popFromHeap(maxHeap, needPopMax);
  popFromHeap(minHeap, needPopMin);

  const maxValue = maxHeap.heapPop();
  const minValue = minHeap.heapPop();

  answer[0] = maxValue || 0;
  answer[1] = -minValue || 0; 

  return answer;
};

function seperate(operation) {
  const operationArray = operation.split(" ");
  const order = operationArray[0];
  const number = Number(operationArray[1]);

  return [order, number];
};

function popFromHeap(targetHeap, needPopMap) {
  const target = targetHeap.heap[1];

  while (needPopMap.has(target) && needPopMap.get(target) > 0) {
    needPopMap.set(target, needPopMap.get(target) - 1);
    targetHeap.heapPop();
  };
};

function addToMap(target, needPopMap) {
  if (target === null) {
    return;
  };

  if (!needPopMap.has(target)) {
    needPopMap.set(target, 1);
  } else {
    needPopMap.set(target, needPopMap.get(target) + 1);
  };
};

class Heap {
  constructor() {
    this.heap = [0];
  };

  heapPush(x) {
    this.heap.push(x);
    let childIdx = this.heap.length - 1;
    let child = this.heap[childIdx];

    while (childIdx >= 2) {
      const parentIdx = parseInt(childIdx / 2);
      const parent = this.heap[parentIdx];

      if (parent < child) {
        this.heap[parentIdx] = child;
        this.heap[childIdx] = parent;
        childIdx = parentIdx;
      } else {
        break;
      };
    };
  };

  heapPop() {
    let result = null;

    if (this.heap.length === 1) {
      return result;
    };

    let lastIdx = this.heap.length - 1;
    let parentIdx = 1;
    let parent = this.heap[lastIdx];

    result = this.heap[1];
    this.heap[parentIdx] = this.heap[lastIdx];
    this.heap.pop();
    
    lastIdx -= 1;

    while (parentIdx * 2 <= lastIdx) {
      let childIdx = parentIdx * 2;
      let child = this.heap[childIdx];

      if (childIdx + 1 <= lastIdx) {
        const rightChild = this.heap[childIdx + 1];

        if (child < rightChild) {
          child = rightChild;
          childIdx += 1;
        };
      };

      if (parent < child) {
        this.heap[parentIdx] = child;
        this.heap[childIdx] = parent;
        parentIdx = childIdx;
      } else {
        break;
      };
    };

    return result;
  };
};

// console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]));
console.log(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]));