function solution(s) {
  let changeCount = 0;
  let deleteZeroCount = 0;
  let target = s.split('').map(element => Number(element));

  while (target.join('') !== '1') {
    let beforeLength = target.length;
    let afterDeleteZeroLength = target.filter(element => element === 1).length;
    changeCount += 1;
    deleteZeroCount += beforeLength - afterDeleteZeroLength;
    target = [...makeBinary(afterDeleteZeroLength)];
    console.log(target)
  };

  return [changeCount, deleteZeroCount];
};

function makeBinary(number) {
  let result = [];

  while (number > 1) {
    let remain = number % 2;
    number = parseInt(number / 2);
    result = [remain, ...result];
  };

  result = [number, ...result];
  return result;
};

console.log(solution('110010101001'));