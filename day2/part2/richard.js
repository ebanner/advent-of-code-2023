const fs = require('node:fs');

function getCubeCounts(unprocessedDrawString) {
  // E.g. '1 red, 2 green 6 blue' => ['1 red', '2 green', '6 blue']:
  const cubeStrings = unprocessedDrawString.trim().split(',');

  const cubeCounts = {
    red: 0,
    green: 0,
    blue: 0,
  };
  cubeStrings.forEach((cubeDrawString) => {
    // E.g. '6 blue' => ['6', 'blue']:
    const [count, cube] = cubeDrawString.trim().split(' ');
    cubeCounts[cube] = parseInt(count, 10);
  });
  return cubeCounts;
}

function getGamePower(cubeCounts) {
  return cubeCounts.red * cubeCounts.green * cubeCounts.blue;
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

  const requiredNumberOfCubes = {
    red: 0,
    green: 0,
    blue: 0,
  };
  draws.forEach((draw) => {
    cubeCounts = getCubeCounts(draw);
    requiredNumberOfCubes.red = Math.max(cubeCounts.red, requiredNumberOfCubes.red);
    requiredNumberOfCubes.green = Math.max(cubeCounts.green, requiredNumberOfCubes.green);
    requiredNumberOfCubes.blue = Math.max(cubeCounts.blue, requiredNumberOfCubes.blue);
  });
  return getGamePower(requiredNumberOfCubes);
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
    const powersSum = fileContents
      .split('\n')
      .reduce((total, nextLine) => total + processLine(nextLine.toLowerCase()), 0);
    console.log({ powersSum });
  });
}

main();
