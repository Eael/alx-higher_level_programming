#!/usr/bin/node
/* A script that prints a square
 * First argument is the size of the square
 */

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const num = Number(process.argv[2]);
  let i = 0;
  while (i < num) {
    console.log('x'.repeat(num));
    i++;
  }
}
