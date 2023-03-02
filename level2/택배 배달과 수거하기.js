function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let deliveryIndex = n - 1;
  let pickupIndex = n - 1;

  while (true) {
    let possibleDeliveryMount = cap;
    let deliveryDistance = 0;

    for (let i = deliveryIndex; i >= 0; i--) {
      if (deliveries[i] !== 0 && deliveryDistance === 0) {
        deliveryDistance = i + 1;
      };

      if (deliveries[i] <= possibleDeliveryMount) {
        possibleDeliveryMount -= deliveries[i];
        deliveries[i] = 0;
      } else {
        deliveries[i] -= possibleDeliveryMount;
        possibleDeliveryMount = 0;
      };

      if (possibleDeliveryMount === 0) {
        break;
      };

      deliveryIndex = i;
    };

    let possiblePickupMount = cap;
    let pickupDistance = 0;

    for (let i = pickupIndex; i >= 0; i--) {
      if (pickups[i] !== 0 && pickupDistance === 0) {
        pickupDistance = i + 1;
      };

      if (pickups[i] <= possiblePickupMount) {
        possiblePickupMount -= pickups[i];
        pickups[i] = 0;
      } else {
        pickups[i] -= possiblePickupMount;
        possiblePickupMount = 0;
      };

      if (possiblePickupMount === 0) {
        break;
      };

      pickupIndex = i;
    };

    if (pickupDistance + deliveryDistance === 0) {
      break;
    };

    answer += Math.max(pickupDistance, deliveryDistance);
  };

  return answer * 2;
};

console.log(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]));
console.log(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]));