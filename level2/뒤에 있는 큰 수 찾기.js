function solution(numbers) {
  const answer = new Array(numbers.length).fill(-1);

  for (let i = 0; i < numbers.length; i++) {
    const current = numbers[i];

    for (let j = i + 1; j < numbers.length; j++) {
      const nextNumber = numbers[j];
      let isExist = false;

      if (nextNumber > current) {
        answer[i] = nextNumber;
        isExist = true;
        break;
      };

      if (isExist) answer[i] = -1;
    };
  };

  return answer;
}