fn main() {
    // [i32; 3] type and size
    // here i32 is superfluous
    let scores: [i32; 3] = [72, 73, 33];
    let average: f32 = array_average(scores);

    // no implicit casting. 
    println!("Average: {}", average);
}

// size of array must be known
fn array_average(scores: [i32; 3]) -> f32 {
    println!("Array length: {}", scores.len());

    // variables are immutable by default. 
    let mut total = 0;

    for index in 0..3 {
        total += scores[index];
        println!("Total: {}, {}", total, scores[index]);
    }   

    println!("Total: {}", total);

    return total as f32 / (scores.len() as f32);
}