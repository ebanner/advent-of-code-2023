const fs = require('node:fs');

function extractSortedNumbersFromString(str) {
  return str
    .split(' ')
    .filter((num) => !!num)
    .map((num) => parseInt(num, 10))
    .sort();
}

function processLine(line, lineIndex, cardCounts) {
  cardCounts[lineIndex] += 1;
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
  for (let i = 0; i < numMatches; i++) {
    cardCounts[lineIndex + i + 1] += cardCounts[lineIndex];
  }
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
    const cardCounts = fileLines.map((_) => 0);
    fileLines.forEach((nextLine, lineIndex) => processLine(nextLine, lineIndex, cardCounts));
    const total = cardCounts.reduce((total, next) => total + next, 0);
    console.log({ total });
  });
}

main();
