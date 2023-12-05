const fs = require('node:fs');

function isDigit(value) {
  return !isNaN(parseInt(value));
}

function isSymbol(value) {
  return !isDigit(value) && value !== '.';
}

function isSymbolNextTo(lines, lineIndex, charIndex) {
  const linesToCheck = [lines[lineIndex]];
  if (lineIndex > 0) {
    linesToCheck.push(lines[lineIndex - 1]);
  }
  if (lineIndex < lines.length - 1) {
    linesToCheck.push(lines[lineIndex + 1]);
  }
  for (let i = 0; i < linesToCheck.length; i++) {
    const lineToCheck = linesToCheck[i];
    if (isSymbol(lineToCheck.charAt(charIndex))) {
      return true;
    }
    if (charIndex > 0 && isSymbol(lineToCheck.charAt(charIndex - 1))) {
      return true;
    }
    if (charIndex < lineToCheck.length - 1 && isSymbol(lineToCheck.charAt(charIndex + 1))) {
      return true;
    }
  }
  return false;
}

function isPartNumberAdjacentToSymbol(lines, lineIndex, partNumberStartIndex, partNumber) {
  for (let i = 0; i < partNumber.length; i++) {
    if (isSymbolNextTo(lines, lineIndex, partNumberStartIndex + i)) {
      return true;
    }
  }
  return false;
}

function processFile(fileContents) {
  let partNumberSum = 0;
  const lines = fileContents.split('\n');
  lines.forEach((line, lineIndex) => {
    let curRunningPartNumber = '';
    for (let i = 0; i < line.length; i++) {
      const nextChar = line.charAt(i);
      if (isDigit(nextChar)) {
        curRunningPartNumber += nextChar;
      } else {
        const startOfRunIndex = i - curRunningPartNumber.length;
        if (isPartNumberAdjacentToSymbol(lines, lineIndex, startOfRunIndex, curRunningPartNumber)) {
          const partNumber = parseInt(curRunningPartNumber, 10);
          partNumberSum += partNumber;
        }
        curRunningPartNumber = '';
      }
    }
    if (
      isPartNumberAdjacentToSymbol(
        lines,
        lineIndex,
        line.length - curRunningPartNumber.length,
        curRunningPartNumber
      )
    ) {
      const partNumber = parseInt(curRunningPartNumber, 10);
      partNumberSum += partNumber;
    }
  });
  return partNumberSum;
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
