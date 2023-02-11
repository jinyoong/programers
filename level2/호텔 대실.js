function solution(book_time) {
  let answer = 0;
  const times = new Array(60 * 24 + 1).fill(0);

  for (let bookTime of book_time) {
    const checkIn = bookTime[0].split(":").map(element => Number(element)).reduce((prev, curr) => prev * 60 + curr);
    const checkOut = bookTime[1].split(":").map(element => Number(element)).reduce((prev, curr) => prev * 60 + curr) + 10;

    times[checkIn] += 1;
    times[checkOut] -= 1;
  };

  for (let i = 1; i < 60 * 24 + 1; i++) {
    times[i] = times[i - 1] + times[i];
    if (times[i] > answer) answer = times[i];
  }

  return answer;
};

console.log(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
console.log(solution([["09:00", "10:00"], ["10:10", "10:20"]]))