import * as fs from 'fs';


interface Position {
  x: number;
  y: number;
}


const loadInput = (fileName: string): string =>
  fs.readFileSync(fileName, 'utf8');

const splitInput = (input: string): string[][] =>
  input.split('\n').map(line => line.split(''));

const keypad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

const move = (position: Position, instruction: string): Position => {
  const newRawPosition = {
    x: position.x - (instruction === 'L' ? 1 : 0) + (instruction === 'R' ? 1 : 0),
    y: position.y - (instruction === 'U' ? 1 : 0) + (instruction === 'D' ? 1 : 0),
  };
  return {
    x: Math.min(Math.max(newRawPosition.x, 0), 2),
    y: Math.min(Math.max(newRawPosition.y, 0), 2),
  };
};

const solution1 = (input: string): string => {
  const initialPosition: Position = {x: 1, y: 1};
  const instructions = splitInput(input);
  let bathroomCode: number[] = [];
  let position = initialPosition;
  instructions.forEach((lineOfInstructions, _) => {
    lineOfInstructions.forEach((instruction, _) => {
      position = move(position, instruction);
    });
    bathroomCode.push(keypad[position.y][position.x]);
  });
  return bathroomCode.map((codeNum, _) => codeNum.toString()).join('');
};

const keypad2 = [
  [null, null, '1', null, null],
  [null, '2', '3', '4', null],
  ['5', '6', '7', '8', '9'],
  [null, 'A', 'B', 'C', null],
  [null, null, 'D', null, null],
];

const move2 = (position: Position, instruction: string): Position => {
  const newRawPosition = {
    x: position.x - (instruction === 'L' ? 1 : 0) + (instruction === 'R' ? 1 : 0),
    y: position.y - (instruction === 'U' ? 1 : 0) + (instruction === 'D' ? 1 : 0),
  };
  const newRawPosition2 = {
    x: Math.min(Math.max(newRawPosition.x, 0), 4),
    y: Math.min(Math.max(newRawPosition.y, 0), 4),
  };
  return {
    x: keypad2[position.y][newRawPosition2.x] !== null ? newRawPosition2.x : position.x,
    y: keypad2[newRawPosition2.y][position.x] !== null ? newRawPosition2.y : position.y,
  };
};

const solution2 = (input: string): string => {
  const initialPosition: Position = {x: 0, y: 2};
  const instructions = splitInput(input);
  let bathroomCode: (string | null)[] = [];
  let position = initialPosition;
  instructions.forEach((lineOfInstructions, _) => {
    lineOfInstructions.forEach((instruction, _) => {
      position = move2(position, instruction);
    });
    bathroomCode.push(keypad2[position.y][position.x]);
  });
  return bathroomCode.join('');
};


const input = loadInput('input');

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
