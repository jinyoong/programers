function solution(s) {
  let maximum = -987654321;
  let minimum = 987654321;
  const numbers = s.split(" ");

  numbers.forEach(element => {
    const number = Number(element);
    if (number > maximum) maximum = number;

    if (number < minimum) minimum = number;
  })

  return [minimum, maximum].join(" ");
};

console.log(solution("1 2 3 4"));