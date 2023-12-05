const fs = require('node:fs');

function isDigit(char) {
  return char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
}

function isSymbol(char) {
  return !isDigit(char) && char !== '.';
}

function isCharIndexNearSymbol(charIndex, line) {
  if (charIndex > 0 && isSymbol(line.charAt(charIndex - 1))) {
    return true;
  }
  if (charIndex < line.length - 1 && isSymbol(line.charAt(charIndex + 1))) {
    return true;
  }
  return false;
}

function processFile(fileContents) {
  const fileLines = fileContents.split('\n');
  const replacedLines = [];
  const count = fileLines.reduce((partNumbersSum, line, lineIndex) => {
    replacedLines.push(line);
    const partNumbersFound = [];
    let i = 0;
    while (i < line.length) {
      // Not a digit, so skip to next character:
      if (!isDigit(line.charAt(i))) {
        i++;
        continue;
      }
      // Is a digit, so collect all digits and see if any are near a symbol:
      let nextPartNumber = '';
      let isNearSymbol = false;
      while (i < line.length && isDigit(line.charAt(i))) {
        // Check line above:
        if (!isNearSymbol && lineIndex > 0) {
          isNearSymbol |= isCharIndexNearSymbol(i, fileLines[lineIndex - 1]);
        }
        // Check this line:
        if (!isNearSymbol) {
          isNearSymbol |= isCharIndexNearSymbol(i, line);
        }
        // Check line below:
        if (!isNearSymbol && lineIndex < fileLines.length - 1) {
          isNearSymbol |= isCharIndexNearSymbol(i, fileLines[lineIndex + 1]);
        }
        nextPartNumber += line.charAt(i);
        i++;
      }
      if (isNearSymbol) {
        partNumbersFound.push(nextPartNumber);
        replacedLines[lineIndex] = replacedLines[lineIndex] + 'X';
      }
    }
    const sumForLine = partNumbersFound.reduce(
      (sum, nextPartNumber) => sum + parseInt(nextPartNumber, 10),
      0
    );
    // console.log({ line, partNumbersFound, sumForLine });
    return sumForLine + partNumbersSum;
    // return partNumbersFound.reduce(
    //   (sum, nextPartNumber) => sum + parseInt(nextPartNumber, 10),
    //   partNumbersSum
    // );
  }, 0);
  // console.log(replacedLines.join('\n'));
  return count;
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
    console.log({ partNumbersSum: processFile(fileContents) });
  });
}

main();
