function solution(wallpaper) {
  let answer = [100, 100, 0, 0];
  let width = wallpaper[0].length;
  let height = wallpaper.length;

  for (let r = 0; r < height; r++) {
    for (let c = 0; c < width; c++) {
      if (wallpaper[r][c] === '.') {
        continue;
      };

      const [top, left, bottom, right] = [r, c, r + 1, c + 1];

      if (answer[0] > top) {
        answer[0] = top;
      };

      if (answer[1] > left) {
        answer[1] = left;
      };

      if (answer[2] < bottom) {
        answer[2] = bottom;
      }; 

      if (answer[3] < right) {
        answer[3] = right;
      };
    };
  };

  return answer;
};

console.log(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))