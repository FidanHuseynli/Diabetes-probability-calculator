fn euclidean_distance(p1: &[f64], p2: &[f64]) -> f64 {
    let sum: f64 = p1.iter()
        .zip(p2.iter())
        .map(|(a, b)| (a - b) * (a - b))
        .sum();
    sum.sqrt()
}

fn main() {
    let point1 = [6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0];
    let point2 = [1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0];
    println!("Euclidean Distance: {}", euclidean_distance(&point1, &point2));
}