package main

import "fmt"

func main() {
	scores := []int{72, 73, 33}

	fmt.Printf("Array length: %d\n", len(scores))

	var average = array_average(scores)
	fmt.Printf("Average: %f\n", average)
}

func array_average(scores []int) float32 {
	var total = 0 // type can be inferred

	for i := 0; i < len(scores); i++ {
		total += scores[i]
		fmt.Printf("Total: %d, %d\n", total, scores[i])
	}

	fmt.Printf("Total: %d\n", total)

	// have to cast both vars?
	return float32(total) / float32(len(scores))
}
