import * as fs from 'fs';


export const loadInput = (fileName: string): string =>
  fs.readFileSync(fileName, 'utf8');
