function solution(park, routes) {
  const width = park[0].length;
  const height = park.length;
  const directions = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]};
  let position = [-1, -1];

  for (let r = 0; r < height; r++) {
    if (position[0] !== -1) {
      break;
    };

    for (let c = 0; c < width; c++) {
      const element = park[r][c];

      if (element === 'S') {
        position = [r, c];
        break;
      };
    };
  };

  for (let element of routes) {
    const route = element.split(" ");
    const direction = directions[route[0]];
    const weight = Number(route[1]);
    let isBreak = false;
    let nr;
    let nc;

    for (let i = 1; i <= weight; i++) {
      nr = position[0] + direction[0] * i;
      nc = position[1] + direction[1] * i;

      if (nr < 0 || nr >= height || nc < 0 || nc >= width) {
        isBreak = true;
        break;
      };
  
      if (park[nr][nc] === 'X') {
        isBreak = true;
        break;
      };
    };

    if (!isBreak) {
      position = [nr, nc];
    };
  };

  return position;
};

console.log(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]));
console.log(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]));
console.log(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]));