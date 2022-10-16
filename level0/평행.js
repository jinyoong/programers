function solution(dots) {
  var answer = 0;
  let possibleArray = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]];
  
  possibleArray.map((possible) => {
    let inc1;
    let inc2;
    let first = possible[0]
    let second = possible[1]
    let third = possible[2]
    let last = possible[3]

    if (dots[first][0] === dots[second][0]) {
      if (dots[third[0] === dots[last][0] ]) {
        answer += 1
      }
    } else {
      inc1 = (dots[first][1] - dots[second][1]) / (dots[first][0] - dots[second][0])
      inc2 = (dots[third][1] - dots[last][1]) / (dots[third][0] - dots[last][0])

      if (inc1 === inc2) {
        console.log("같음")
        answer += 1
      }
    }

  })

  if (answer > 0) {
    return 1;
  } else {
    return 0
  }
}