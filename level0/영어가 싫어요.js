function solution(numbers) {
  let answer = 0;
  let number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  let tempNum = "";

  for (let i = 0; i < numbers.length; i++) {
    tempNum += numbers[i]

    if (number.indexOf(tempNum) != -1) {
      answer = answer * 10 + number.indexOf(tempNum)
      tempNum = ""
    }
  }

  return answer;
}