var scores = [72, 73, 33];
console.log("Array length: ".concat(scores.length));
var total = 0;
for (var i = 0; i < scores.length; i++) {
    total += scores[i];
    console.log("Total: ".concat(total, ", ").concat(scores[i]));
}
console.log("Total: ".concat(total));
console.log("Average: ".concat(total / scores.length));
