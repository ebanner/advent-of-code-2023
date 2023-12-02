const fs = require('node:fs');

const MAX_DRAW_LIMIT_MAP = {
  red: 12,
  green: 13,
  blue: 14,
};

function isDrawValid(unprocessedDrawString) {
  // E.g. '1 red, 2 green 6 blue' => ['1 red', '2 green', '6 blue']:
  const cubeStrings = unprocessedDrawString.trim().split(',');

  let isValid = true;
  cubeStrings.forEach((cubeDrawString) => {
    // E.g. '6 blue' => ['6', 'blue']:
    const [count, cube] = cubeDrawString.trim().split(' ');
    if (parseInt(count, 10) > MAX_DRAW_LIMIT_MAP[cube]) {
      isValid = false;
    }
  });
  return isValid;
}

function processLine(line) {
  // E.g. 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
  //   => ['Game 1', '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']:
  const [gameIDPart, cubeDrawsPart] = line.split(':');

  // E.g. 'Game 1' => '1':
  const gameID = gameIDPart.substring('game '.length);

  // E.g. '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
  //   => ['3 blue, 4 red', '1 red, 2 green 6 blue', '2 green']
  const draws = cubeDrawsPart.split(';');

  const isValid = draws.every((draw) => isDrawValid(draw));
  return isValid ? parseInt(gameID, 10) : 0;
}

function main() {
  const fileName = process.argv[2];
  if (!fileName) {
    console.error('Please pass in a file name, e.g. node richard.js data/test.txt');
    return;
  }
  fs.readFile(fileName, 'utf8', (err, fileContents) => {
    if (err) {
      console.error(err);
      return;
    }
    const idSum = fileContents
      .split('\n')
      .reduce((total, nextLine) => total + processLine(nextLine.toLowerCase()), 0);
    console.log({ idSum });
  });
}

main();
