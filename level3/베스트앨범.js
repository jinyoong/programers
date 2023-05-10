function solution(genres, plays) {
  let answer = [];
  let genreNames = [];
  let bestOfGenre = {};

  for (let i = 0; i < genres.length; i++) {
    const genre = genres[i];
    const play = plays[i];

    if (!bestOfGenre.hasOwnProperty(genre)) {
      bestOfGenre[genre] = [play, [i, play], [-1, -1]];
      genreNames.push(genre);
    } else {
      const first = bestOfGenre[genre][1][1];
      const second = bestOfGenre[genre][2][1];

      bestOfGenre[genre][0] += play;
      
      if (play > first) {
        bestOfGenre[genre][2] = [...bestOfGenre[genre][1]];
        bestOfGenre[genre][1] = [i, play];
      } else if (play > second) {
        bestOfGenre[genre][2] = [i, play];
      };
    };
  };

  genreNames
    .sort((a, b) => bestOfGenre[b][0] - bestOfGenre[a][0])
    .forEach(genre => {
      for (let i = 1; i < 3; i++) {
        const idx = bestOfGenre[genre][i][0];

        if (idx !== -1) {
          answer.push(idx);
        };
      };
    });

  return answer;
};

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]));