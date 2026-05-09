var point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50];
var point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31];

function euclideanDistance(p1, p2) {
    var sum = 0;
    for (var i = 0; i < p1.length; i++) {
        sum += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    }
    return Math.sqrt(sum);
}

console.log("Euclidean Distance: " + euclideanDistance(point1, point2));
