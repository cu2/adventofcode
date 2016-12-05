import * as fs from 'fs';


interface Triangle {
  a: number;
  b: number;
  c: number;
}


const loadInput = (fileName: string): string =>
  fs.readFileSync(fileName, 'utf8');

const parseInput = (input: string): Triangle[] => {
  const rawTriangles = input.split('\n').map((line, _) => line.match(/\S+/g));
  let filteredRawTriangles: RegExpMatchArray[] = [];  // filter doesn't fix the type :-(
  rawTriangles.forEach((rawTriangle, _) => {
    if (rawTriangle !== null) {
      filteredRawTriangles.push(rawTriangle);
    }
  });
  return filteredRawTriangles.map((rawTriangle, _) => {
    const sides = rawTriangle.map((matchElem, _) => parseInt(matchElem));
    return {
      a: sides[0],
      b: sides[1],
      c: sides[2],
    };
  });
};

const cutIntoTrios = <T>(list: T[]): T[][] => {
  let trios: T[][] = [];
  let trio: T[] = [];
  list.forEach((item, index) => {
    trio.push(item);
    if (index % 3 === 2) {
      trios.push(trio);
      trio = [];
    }
  });
  return trios;
};

const transposeTrio = (triangleTrio: Triangle[]): Triangle[] =>
  [
    {
      a: triangleTrio[0].a,
      b: triangleTrio[1].a,
      c: triangleTrio[2].a,
    },
    {
      a: triangleTrio[0].b,
      b: triangleTrio[1].b,
      c: triangleTrio[2].b,
    },
    {
      a: triangleTrio[0].c,
      b: triangleTrio[1].c,
      c: triangleTrio[2].c,
    },
  ];

const transposeInput = (triangles: Triangle[]): Triangle[] => {
  const triangleTrios = cutIntoTrios(triangles);
  return (<Triangle[]>[]).concat(...triangleTrios.map((triangleTrio, _) => transposeTrio(triangleTrio)));
};

const isValidTriangle = (triangle: Triangle): boolean =>
  (triangle.a + triangle.b > triangle.c) &&
  (triangle.b + triangle.c > triangle.a) &&
  (triangle.c + triangle.a > triangle.b);

const solution1 = (input: string): number => {
  const triangles = parseInput(input);
  return triangles.filter((triangle, _) => isValidTriangle(triangle)).length; 
};

const solution2 = (input: string): number => {
  const triangles = transposeInput(parseInput(input));
  return triangles.filter((triangle, _) => isValidTriangle(triangle)).length; 
};


const input = loadInput('input');

const output1 = solution1(input);
console.log(output1);

const output2 = solution2(input);
console.log(output2);
