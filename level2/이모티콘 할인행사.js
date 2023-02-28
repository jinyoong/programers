function solution(users, emoticons) {
  let answer = [0, 0];
  const SALES = [40, 30, 20, 10];

  let saleArray = [];

  function makeSales(idx, result) {
    
    if (idx === emoticons.length) {
      saleArray.push(result);
      return;
    };

    for (let element of SALES) {
      makeSales(idx + 1, [...result, element]);
    };
  };

  makeSales(0, []);

  saleArray.forEach(saleElement => {
    let plusCount = 0;
    let totalProfit = 0;

    users.forEach(user => {
      let buyResult = 0;
      const want = user[0];
      const limit = user[1];

      emoticons.forEach((emoticon, index) => {
        if (saleElement[index] >= want) {
          buyResult += parseInt(emoticon * (100 - saleElement[index]) / 100);
        };
      });

      if (buyResult >= limit) {
        plusCount += 1;
      } else {
        totalProfit += buyResult;
      };
    });

    if (plusCount > answer[0]) {
      answer = [plusCount, totalProfit];
    } else if (plusCount === answer[0] && totalProfit > answer[1]) {
      answer[1] = totalProfit;
    };
  });

  return answer;
};

console.log(solution([[40, 10000], [25, 10000]], [7000, 9000]));