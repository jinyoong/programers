function solution(routes) {
  const sortedRoutes = routes.sort((a, b) => a[0] - b[0]);
  let result = [sortedRoutes[0]];

  sortedRoutes.forEach((route) => {
    const start = route[0];
    const end = route[1];
    let isDuplicated = false;

    for (let i = 0; i < result.length; i++) {
      let camera = result[i];
      let cameraStart = camera[0];
      let cameraEnd = camera[1];
      
      if (cameraEnd < start) {
        continue;
      } else {
        cameraStart = Math.max(cameraStart, start);
        cameraEnd = Math.min(cameraEnd, end);
        isDuplicated = true;
        result[i] = [cameraStart, cameraEnd];
        break;
      };
    };

    if (!isDuplicated) {
      result.push([start, end]);
    };
  });

  return result.length;
};

console.log(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]));