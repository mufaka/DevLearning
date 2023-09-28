package main

import "fmt"

func main() {
	scores := [3]int{72, 73, 33}

	fmt.Printf("Array length: %d\n", len(scores))

	var total = 0 // type can be inferred

	for i := 0; i < len(scores); i++ {
		total += scores[i]
		fmt.Printf("Total: %d, %d\n", total, scores[i])
	}

	// have to cast both vars?
	var average float64 = float64(total) / float64(len(scores))

	fmt.Printf("Total: %d\n", total)
	fmt.Printf("Average: %f\n", average)
}
