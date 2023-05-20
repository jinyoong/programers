function solution(tickets) {
  let answer = [];
  let cityObject = makeObject(tickets);
  const allCityCount = allCities(tickets).size;

  console.log(cityObject);

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

  return result;
}

console.log(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]));
console.log(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]));