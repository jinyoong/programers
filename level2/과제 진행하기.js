function solution(plans) {
  let answer = [];
  let inStop = [];
  let inProgress = [0, 0, 0];
  let idx = 0;
  const sortedPlans = plans.sort((a, b) => calculateTime(a[1]) - calculateTime(b[1]));

  while (idx < sortedPlans.length) {
    // 새로 시작해야 하는 과제의 정보
    const name = sortedPlans[idx][0];
    const startTime = calculateTime(sortedPlans[idx][1]);
    const remainTime = Number(sortedPlans[idx][2]);
    const progressEndTime = inProgress[1] + inProgress[2];

    if (progressEndTime === startTime) {
      if (typeof inProgress[0] === "string") {
        answer.push(inProgress[0]);
      };

      inProgress = [name, startTime, remainTime];
      idx += 1;
    } else if (progressEndTime > startTime) {
      // 진행 중인 과제가 끝날 시간이 새로 시작해야 하는 과제의 시작 시간보다 늦는 경우
      inStop.push([inProgress[0], startTime, progressEndTime - startTime]);
      inProgress = [name, startTime, remainTime];
      idx += 1;
    } else {
      // 진행 중인 과제가 끝나고 어느 정도의 시간이 흐른 뒤에 과제를 시작하는 경우
      if (typeof inProgress[0] === "string") {
        answer.push(inProgress[0]);
      };

      let blankTime = startTime - progressEndTime;

      if (inStop.length === 0) {
        // 중간에 멈춘 과제가 없는 경우
        inProgress = [name, startTime, remainTime];
        idx += 1;
      } else {
        let latestStopPlan = inStop.pop();
  
        while (latestStopPlan !== undefined && latestStopPlan[2] <= blankTime) {
          blankTime -= latestStopPlan[2];
          answer.push(latestStopPlan[0]);
  
          latestStopPlan = inStop.pop();
        };

        if (latestStopPlan !== undefined) {
          inStop.push([latestStopPlan[0], startTime, latestStopPlan[2] - blankTime]);
        };
        
        inProgress = [name, startTime, remainTime];
        idx += 1;
      };
    };
  };

  answer.push(inProgress[0]);
  
  for (let stopPlan of inStop.reverse()) {
    answer.push(stopPlan[0]);
  };

  return answer;
};

function calculateTime(timeOfString) {
  const timeArray = timeOfString.split(":");
  const result = Number(timeArray[0]) * 60 + Number(timeArray[1]);
  
  return result;
};

console.log(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]));
console.log(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]));
console.log(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
console.log(solution([["aaa", "12:00", "26"], ["bbb", "12:25", "5"], ["ccc", "12:31", "1"]]))