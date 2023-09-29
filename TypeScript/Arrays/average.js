function array_average(scores) {
    var total = 0;
    for (var i = 0; i < scores.length; i++) {
        total += scores[i];
        console.log("Total: ".concat(total, ", ").concat(scores[i]));
    }
    console.log("Total: ".concat(total));
    return total / scores.length;
}
var scores = [72, 73, 33];
console.log("Array length: ".concat(scores.length));
var average = array_average(scores);
console.log("Average: ".concat(average));
