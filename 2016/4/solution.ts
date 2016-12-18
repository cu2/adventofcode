import { loadInput } from '../utils';


interface RoomCode {
  encryptedName: string;
  sectorID: number;
  checksum: string;
}

interface ExtendedRoomCode extends RoomCode {
  decryptedName: string;
}


const parseRoomCode = (rawCode: string): RoomCode | null => {
  const code = rawCode.match(/([a-z-]+)-([0-9]+)\[(.{5})\]/);
  if (code === null) {
    return null;
  }
  return {
    encryptedName: code[1],
    sectorID: parseInt(code[2]),
    checksum: code[3],
  };
};

const parseInput = (input: string): RoomCode[] =>
  <RoomCode[]>input.split('\n').map((rawCode, _) => parseRoomCode(rawCode)).filter((item, _) => item !== null);

const computeChecksum = (encryptedName: string): string => {
  let charCount: { [char: string]: number } = {};
  encryptedName.split('').filter((char, _) => char.match(/[a-z]/)).forEach((char, _) => {
    if (!(char in charCount)) {
      charCount[char] = 0;
    }
    charCount[char] += 1;
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
  return charCountList.slice(0, 5).map((item, _) => item[1]).join('');
};

const decodeChar = (ch: string, sectorID: number): string =>
  ch === '-' ? ' ' : (
    String.fromCharCode((((ch.charCodeAt(0) - 97) + sectorID) % 26) + 97)
  );

const decodeRoom = (roomCode: RoomCode): string =>
  roomCode.encryptedName.split('').map(ch => decodeChar(ch, roomCode.sectorID)).join('');

const solution1 = (input: string): number => {
  const rooms = parseInput(input);
  const realRooms = rooms.filter((room, _) => computeChecksum(room.encryptedName) === room.checksum);
  return realRooms.map((room, _) => room.sectorID).reduce((a, b) => a + b, 0);
};

const solution2 = (input: string): ExtendedRoomCode[] => {
  const rooms = parseInput(input);
  const realRooms = rooms.filter((room, _) => computeChecksum(room.encryptedName) === room.checksum);
  return realRooms
    .map((roomCode: RoomCode) => Object.assign({}, roomCode, { decryptedName: decodeRoom(roomCode) }))
    .filter((extendedRoomCode: ExtendedRoomCode) => extendedRoomCode.decryptedName.indexOf('north') !== -1);
};

const input = loadInput('input');

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
