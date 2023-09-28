// node average.js
scores = [ 72, 73, 33 ]; 
console.log(`Array length: ${scores.length}`);

total = 0;

for (i = 0; i < scores.length; ++i) 
{
    total += scores[i];
    console.log(`Total: ${total}, ${scores[i]}`);
}

console.log(`Total: ${total}`);
console.log(`Average: ${total / scores.length}`);