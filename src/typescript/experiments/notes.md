# TypeScript
## Compiling
- tsc to convert ts to js and then use node to run. tsc is typescript compiler.
  - tsc app.ts -> app.js. node app.js -> run
  - Must be done to view on html page; in html, js is linked.
  - Updates made to .ts, run tsc, updates seen.
- tsx to run without compiling js
  - tsx app.ts -> run

  ## Types
Can assign types
var x: string; // Initialises a variable with identifier x that can only be a string.
let arrayName: number[]; // Init array which can only be an array of numbers.
let person: {
  name: string;
  age: number;
}; // Init person object which can only have 2 attributes: name which must be a string, and age which must be a number.
let greeting : (name: string) => string; // Init a variable which calls a function, taking in a string parameter and returning another string.