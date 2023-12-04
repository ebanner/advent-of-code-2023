const fs = require('node:fs');

function extractSortedNumbersFromString(str) {
  return str
    .split(' ')
    .filter((num) => !!num)
    .map((num) => parseInt(num, 10))
    .sort();
}

function processLine(line) {
  const [_, numbersPart] = line.split(':');
  const [winningNumbersString, yourNumbersString] = numbersPart.split('|');

  const winningNumbers = extractSortedNumbersFromString(winningNumbersString);
  const yourNumbers = extractSortedNumbersFromString(yourNumbersString);

  const numMatches = yourNumbers.reduce((totalNumMatches, nextNumber) => {
    if (winningNumbers.indexOf(nextNumber) >= 0) {
      return totalNumMatches + 1;
    }
    return totalNumMatches;
  }, 0);
  if (numMatches === 0) {
    return 0;
  }
  return Math.pow(2, numMatches - 1);
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
    const fileLines = fileContents.split('\n');
    const numPoints = fileLines.reduce(
      (totalPoints, nextLine) => totalPoints + processLine(nextLine),
      0
    );
    console.log({ numPoints });
  });
}

main();
