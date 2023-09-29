function array_average(scores) {
    let total: number = 0;

    for (let i = 0; i < scores.length; i++) {
        total += scores[i];
        console.log(`Total: ${total}, ${scores[i]}`);
    }
    
    console.log(`Total: ${total}`);
    return total / scores.length;
}

let scores: number[] = [ 72, 73, 33];
console.log(`Array length: ${scores.length}`);

let average = array_average(scores);

console.log(`Average: ${average}`);
