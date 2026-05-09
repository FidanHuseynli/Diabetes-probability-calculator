package main

import (
    "fmt"
    "math"
)

func euclideanDistance(p1, p2 []float64) float64 {
    sum := 0.0
    for i := 0; i < len(p1); i++ {
        diff := p1[i] - p2[i]
        sum += diff * diff
    }
    return math.Sqrt(sum)
}

func main() {
    point1 := []float64{6, 148, 72, 35, 0, 33.6, 0.627, 50}
    point2 := []float64{1, 85, 66, 29, 0, 26.6, 0.351, 31}
    fmt.Printf("Euclidean Distance: %f\n", euclideanDistance(point1, point2))
}