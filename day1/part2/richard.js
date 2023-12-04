const fs = require('node:fs');

const DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
const DIGITS_WRITTEN_TO_DIGIT = {
  one: '1',
  two: '2',
  three: '3',
  four: '4',
  five: '5',
  six: '6',
  seven: '7',
  eight: '8',
  nine: '9',
};

function isDigit(char) {
  return char in DIGITS;
}

function findAllIndices(haystack, needle) {
  const indices = [];
  let nextIndex = haystack.indexOf(needle);
  while (nextIndex >= 0) {
    indices.push(nextIndex);
    nextIndex = haystack.indexOf(needle, nextIndex + 1);
  }
  return indices;
}

function extractDigits(line) {
  const replaceMap = new Map();
  Object.keys(DIGITS_WRITTEN_TO_DIGIT).forEach((digitWritten) => {
    const indices = findAllIndices(line, digitWritten);
    if (indices.length > 0) {
      replaceMap.set(digitWritten, indices);
    }
  });
  const lineAsChars = line.split('');
  replaceMap.forEach((indices, digitWritten) => {
    indices.forEach((index) => {
      lineAsChars[index] = DIGITS_WRITTEN_TO_DIGIT[digitWritten];
    });
  });
  return lineAsChars.join('');
}

function processLine(line) {
  const convertedLine = extractDigits(line);
  let left, right;
  for (let i = 0; i < convertedLine.length; i++) {
    const nextChar = convertedLine[i];
    if (isDigit(nextChar)) {
      if (left == null) {
        left = nextChar;
      }
      right = nextChar;
    }
  }
  const digits = left + right;
  console.log('processed', { line, convertedLine, digits });
  return parseInt(digits, 10);
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
    const total = fileContents
      .split('\n')
      .reduce((total, nextLine) => total + processLine(nextLine.toLowerCase()), 0);
    console.log({ total });
  });
}

main();
