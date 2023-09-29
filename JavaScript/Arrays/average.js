// node average.js
scores = [ 72, 73, 33 ]; 
console.log(`Array length: ${scores.length}`);

let average = array_average(scores);

console.log(`Average: ${average}`);

function array_average(scores) {
    total = 0;

    for (i = 0; i < scores.length; ++i) {
        total += scores[i];
        console.log(`Total: ${total}, ${scores[i]}`);
    }
    
    console.log(`Total: ${total}`);

    return total / scores.length;
}