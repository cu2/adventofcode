import * as fs from 'fs';


enum Direction {
  Left,
  Right,
}

interface Instruction {
  direction: Direction;
  distance: number;
}

interface Position {
  x: number;
  y: number;
}

enum Heading {
  North,
  East,
  South,
  West,
}

const HeadingCodes = [
  Heading.North,
  Heading.East,
  Heading.South,
  Heading.West,
];

interface State {
  position: Position;
  heading: Heading;
}

const initialState = {
  position: {
    x: 0,
    y: 0,
  },
  heading: Heading.North,
};


const loadInput = (fileName: string): string =>
  fs.readFileSync(fileName, 'utf8');

const splitInput = (input: string): string[] =>
  input.split(',').map( e => e.trim() );

const parseInstruction = (intructionString: string): Instruction => {
  const directionString = intructionString.slice(0, 1);
  const distanceString = intructionString.slice(1);
  return {
    direction: directionString === 'L' ? Direction.Left : Direction.Right,
    distance: parseInt(distanceString),
  };
};

const modHeading = (headingCode: number): number => {
  const rawModHeading = headingCode % 4;
  return (rawModHeading < 0) ? rawModHeading + 4 : rawModHeading;
};

const turn = (heading: Heading, direction: Direction): Heading => {
  const headingCode = HeadingCodes.indexOf(heading);
  const nextHeadingCode = modHeading(headingCode + ((direction === Direction.Left) ? -1 : 1));
  return HeadingCodes[nextHeadingCode];
};

const followInstruction = (state: State, instruction: Instruction): State[] => {
  const nextHeading = turn(state.heading, instruction.direction);
  const unitDelta = {
    x: (nextHeading === Heading.East ? 1 : 0) - (nextHeading === Heading.West ? 1 : 0),
    y: (nextHeading === Heading.North ? 1 : 0) - (nextHeading === Heading.South ? 1 : 0),
  };
  let states: State[] = [];
  for (let step = 1; step <= instruction.distance; step++) {
    states.push({
      position: {
        x: state.position.x + step * unitDelta.x,
        y: state.position.y + step * unitDelta.y,
      },
      heading: nextHeading,
    });
  }
  return states;
};

const followInstructions = (initialState: State, instructionList: Instruction[]): State => {
  let state = initialState;
  instructionList.forEach((instruction, _) => {
    state = followInstruction(state, instruction).pop() || state;
  });
  return state;
};

const positionToString = (position: Position): string =>
  `${position.x},${position.y}`;

const followInstructionsUntilRepeat = (initialState: State, instructionList: Instruction[]): State | null => {
  let history: { [pos: string]: number } = {};
  let state = initialState;
  let finalState: State | null = null;
  history[positionToString(state.position)] = 1;
  instructionList.forEach((instruction, _) => {
    const interStates = followInstruction(state, instruction);
    interStates.forEach((interState, _) => {
      const pos = positionToString(interState.position);
      if (pos in history && finalState === null) {
        finalState = interState;
      }
      history[pos] = 1;
    });
    state = interStates.pop() || state;
  });
  return finalState;
};

const manhattanDistance = (state1: State, state2: State): number =>
  Math.abs(state1.position.x - state2.position.x) +
  Math.abs(state1.position.y - state2.position.y);

const solution1 = (input: string): number => {
  const instructionList = splitInput(input).map(parseInstruction);
  const finalState = followInstructions(initialState, instructionList);
  return manhattanDistance(initialState, finalState);
};

const solution2 = (input: string): number | null => {
  const instructionList = splitInput(input).map(parseInstruction);
  const finalState = followInstructionsUntilRepeat(initialState, instructionList);
  if (finalState === null) {
    return null;
  }
  return manhattanDistance(initialState, finalState);
};


const input = loadInput('input');

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
