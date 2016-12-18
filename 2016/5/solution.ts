import { Md5 } from 'ts-md5/dist/md5';


interface HashCode {
  valid: boolean;
  passwordChar: string;
}

interface NewHashCode extends HashCode {
  passwordPos: number;
}


const getHashCode1 = (doorId: string, index: number): HashCode => {
  const hash = <string>Md5.hashStr(doorId + index.toString(10));
  return {
    valid: hash.slice(0, 5) === '00000',
    passwordChar: hash.slice(5, 6),
  };
};

const solution1 = (input: string): string => {
  let password = '';
  let passwordLength = 0;
  for (let index = 0; ; index++ ) {
    if (index % 1000000 === 0) {
      console.log('[hacking]', index);
    }
    let hashCode = getHashCode1(input, index);
    if (hashCode.valid) {
      password += hashCode.passwordChar;
      passwordLength++;
      console.log('[hacked', passwordLength, 'chars]', password);
    }
    if (passwordLength === 8) {
      return password;
    }
  }
};

const getHashCode2 = (doorId: string, index: number): NewHashCode => {
  const hash = <string>Md5.hashStr(doorId + index.toString(10));
  return {
    valid: hash.slice(0, 5) === '00000',
    passwordPos: parseInt(hash.slice(5, 6), 16),
    passwordChar: hash.slice(6, 7),
  };
};

const solution2 = (input: string): string => {
  let password = '????????';
  let passwordLength = 0;
  for (let index = 0; ; index++ ) {
    if (index % 1000000 === 0) {
      console.log('[hacking]', index);
    }
    let hashCode = getHashCode2(input, index);
    if (hashCode.valid && hashCode.passwordPos < 8 && password.charAt(hashCode.passwordPos) === '?') {
      password = password.slice(0, hashCode.passwordPos) + hashCode.passwordChar + password.slice(hashCode.passwordPos + 1);
      passwordLength++;
      console.log('[hacked', passwordLength, 'chars]', password);
    }
    if (passwordLength === 8) {
      return password;
    }
  }
};


const input = 'wtnhxymk';

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
