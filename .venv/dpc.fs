let point1 = [| 6.0; 148.0; 72.0; 35.0; 0.0; 33.6; 0.627; 50.0 |]
let point2 = [| 1.0; 85.0; 66.0; 29.0; 0.0; 26.6; 0.351; 31.0 |]

let euclideanDistance (p1: float[]) (p2: float[]) =
    Array.map2 (fun a b -> (a - b) * (a - b)) p1 p2
    |> Array.sum
    |> sqrt

printfn "Euclidean Distance: %f" (euclideanDistance point1 point2)