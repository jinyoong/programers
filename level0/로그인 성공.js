function solution(id_pw, db) {
  var answer = 'login';
  let dbObject = {};

  db.map(dbEle => {
    let dbId = dbEle[0];
    let dbPw = dbEle[1];
    dbObject[dbId] = dbPw
  })

  let targetId = id_pw[0]
  let targetPw = id_pw[1]

  if (targetId in dbObject) {
    if (dbObject[targetId] != targetPw) {
      answer = "wrong pw"
    }
  } else {
    answer = "fail"
  }

  return answer;
}