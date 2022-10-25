function solution(A, B) {
  let count = 1;

  if (A === B) {
    return 0
  }

  for (let i = A.length - 1; i > -1; i--) {
    let newA = ""
    for (let j = 0; j < A.length; j++) {
      newA += A[(i + j) % A.length]
    }

    if (newA === B) {
      return count
    }

    count += 1
  }
  return -1
}