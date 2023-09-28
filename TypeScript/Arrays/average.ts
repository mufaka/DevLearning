let scores: number[] = [ 72, 73, 33];
console.log(`Array length: ${scores.length}`);

let total: number = 0;

for (let i = 0; i < scores.length; i++) {
    total += scores[i];
    console.log(`Total: ${total}, ${scores[i]}`);
}

console.log(`Total: ${total}`);
console.log(`Average: ${total / scores.length}`);