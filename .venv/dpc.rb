point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31]

def euclideanDistance(p1, p2)
  sum = 0.0
  p1.length.times do |i|
    sum += (p1[i] - p2[i]) ** 2
  end
  Math.sqrt(sum)
end

puts "Euclidean Distance: #{euclideanDistance(point1, point2)}"