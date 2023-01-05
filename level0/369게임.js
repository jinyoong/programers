function solution(order) {
  return order.toString().split("").filter(element => Number(element) % 3 === 0 && element !== "0").length;
}