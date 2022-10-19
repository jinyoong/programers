function solution(array) {
  var answer = 0;
  let numbers = new Array(1000).fill(0);
  let maximumCount = 0;

  array.forEach((num) => {
    numbers[num] += 1
    if (maximumCount < numbers[num]) {
      maximumCount = numbers[num]
    }
  })

  const finalNum = numbers.filter(ele => ele === maximumCount).length;
  
  if (finalNum > 1) {
    answer = -1;
  } else {
    console.log
    answer = numbers.indexOf(maximumCount);
  }

  return answer;
}