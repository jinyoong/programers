function solution(s, skip, index) {
  let answer = '';

  s.split("").forEach(alpha => {
    let codeNumber = alpha.charCodeAt();
    let count = 0;

    while (count < index) {
      codeNumber = (codeNumber + 1 - 97) % 26 + 97;

      if (skip.includes(String.fromCharCode(codeNumber))) {
        continue;
      };

      count += 1;
    };

    answer += String.fromCharCode(codeNumber);
  })

  return answer;
};

console.log(solution("aukks", "wbqd", 5));