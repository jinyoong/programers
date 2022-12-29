function solution(array) {
  const middle = parseInt(array.length / 2);
  const sortedArray = array.sort((a, b) => a - b)
  return sortedArray[middle];
}