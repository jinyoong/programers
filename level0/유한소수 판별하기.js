function solution(a, b) {
  let target = parseInt(b / gcd(a, b));
  let isBreak = false

  while (target > 1) {
    if (isBreak) return 2;

    for (let number = 2; number <= target; number++) {
      if (!isPrime(number)) continue;

      if (target % number !== 0) continue;

      if (number !== 2 && number !== 5) {
        console.log(number)
        isBreak = true;
        break;
      }

      target = parseInt(target / number);
    }
  }

  return 1;
}

function gcd(n, m) {
  let x = n;
  let y = m;

  while (y > 0) {
    const r = x % y
    x = y;
    y = r;
  }

  return x;
}

function isPrime(n) {
  for (let number = 2; number <= Math.sqrt(n); number++) {
    if (n % number === 0) {
      return false;
    }
  }
  return true;
}