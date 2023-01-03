function solution(cipher, code) {
  return cipher.split("").filter((element, index) => (index + 1) % code === 0).join("");
}