(defvar point1 '(6 148 72 35 0 33.6 0.627 50))
(defvar point2 '(1 85 66 29 0 26.6 0.351 31))

(defun euclidean-distance (p1 p2)
  (sqrt (apply #'+ (mapcar (lambda (a b) (* (- a b) (- a b))) p1 p2))))

(format t "Euclidean Distance: ~f~%" (euclidean-distance point1 point2))