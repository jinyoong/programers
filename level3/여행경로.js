function solution(tickets) {
  let answer = [];
  let cityObject = makeObject(tickets);
  let visited = new Set();
  let result = [];
  let stack = [["ICN", 0, new Set(visited), [...result]]];

  while (stack.length > 0) {
    const [city, usedCount, subVisited, subResult] = stack.pop();

    if (usedCount === tickets.length) {
      answer = [...subResult, city];
      break;
    }

    if (!cityObject.hasOwnProperty(city)) {
      continue;
    }

    const nextCities = cityObject[city];
    
    for (let i = 0; i < nextCities.length; i++) {
      const nextCity = nextCities[i];
      const line = `${city}:${i}`;

      if (subVisited.has(line)) {
        continue;
      }

      let newSubVisited = new Set(subVisited);
      newSubVisited.add(line);

      stack.push([nextCity, usedCount + 1, newSubVisited, [...subResult, city]]);
    }
  }

  return answer;
}

function allCities(tickets) {
  let result = new Set();
  
  for (let ticket of tickets) {
    const start = ticket[0];
    const end = ticket[1];

    result.add(start);
    result.add(end);
  }

  return result;
}

function makeObject(tickets) {
  let result = new Object();

  for (let ticket of tickets) {
    const start = ticket[0];
    const end = ticket[1];

    if (result.hasOwnProperty(start)) {
      result[start].push(end);
    } else {
      result[start] = [end];
    }
  }

  for (let key in result) {
    const value = result[key];
    result[key] = value.sort().reverse();
  }

  return result;
}

console.log(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]));
console.log(solution([["ICN", "SFO"], ["ICN", "SFO"], ["SFO", "ICN"], ["SFO", "ICN"], ["ICN", "DAR"]]))
console.log(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]));