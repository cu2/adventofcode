import { loadInput } from '../utils';


const splitInput = (input: string): string[] =>
  input.split('\n');

const transpose = (listOfStrings: string[]): string[] => {
  if (listOfStrings.length === 0) {
    return [];
  }
  let output: string[] = Array(listOfStrings[0].length).fill('');
  listOfStrings.forEach((inputString, _) => {
    inputString.split('').forEach((inputChar, index) => {
      output[index] += inputChar;
    });
  });
  return output;
};

const charDistribution = (inputString: string): [number, string][] => {
  let charCount: { [char: string]: number } = {};
  inputString.split('').forEach((inputChar) => {
    if (!(inputChar in charCount)) {
      charCount[inputChar] = 0;
    }
    charCount[inputChar] += 1;
  });
  let charCountList: [number, string][] = [];
  Object.keys(charCount).forEach(char => {
    charCountList.push([charCount[char], char]);
  });
  charCountList.sort((a: [number, string], b: [number, string]) => {
    if (a[0] !== b[0]) {
      return b[0] - a[0];
    }
    if (a[1] < b[1]) {
      return -1;
    }
    if (a[1] > b[1]) {
      return 1;
    }
    return 0;
  });
  return charCountList;
};

const mostFrequentChar = (inputString: string): string => {
  const charCountList = charDistribution(inputString);
  return charCountList[0][1];
};

const leastFrequentChar = (inputString: string): string => {
  const charCountList = charDistribution(inputString);
  return charCountList[charCountList.length - 1][1];
};

const solution1 = (input: string): string =>
  transpose(splitInput(input)).map((x) => mostFrequentChar(x)).join('');

const solution2 = (input: string): string =>
  transpose(splitInput(input)).map((x) => leastFrequentChar(x)).join('');


const input = loadInput('input');

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
