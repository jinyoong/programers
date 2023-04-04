function solution(m, n, startX, startY, balls) {
  const answer = balls.map(ball => {
    let minimum = Infinity;

    for (let i = 0; i < 4; i++) {
      const endX = ball[0];
      const endY = ball[1];
      const distance = calculateDistance(m, n, startX, startY, endX, endY, i);

      minimum = Math.min(minimum, distance);
    };

    return minimum;
  });

  return answer;
};

function calculateDistance(m, n, sx, sy, tx, ty, idx) {
  let result;

  if (sx === tx) {
    if (sy < ty && idx === 1) {
      return Infinity;
    };
    
    if (sy > ty && idx === 3) {
      return Infinity;
    };
  };

  if (sy === ty) {
    if (sx < tx && idx === 2) {
      return Infinity;
    };

    if (sx > tx && idx === 0) {
      return Infinity;
    };
  };

  if (idx === 0) {
    // 왼쪽 모서리와 대칭으로 원점 옮긴 경우
    result = (tx + sx) ** 2 + (ty - sy) ** 2;
  } else if (idx === 1) {
    // 위쪽 모서리와 대칭으로 원점 옮긴 경우
    result = (2 * n - ty - sy) ** 2 + (tx - sx) ** 2;
  } else if (idx === 2) {
    // 오른쪽 모서리와 대칭으로 원점 옮긴 경우
    result = (2 * m - tx - sx) ** 2 + (ty - sy) ** 2;
  } else {
    // 아래쪽 모서리와 대칭으로 원점 옮긴 경우
    result = (ty + sy) ** 2 + (tx - sx) ** 2;
  };

  return result;
};

console.log(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]));