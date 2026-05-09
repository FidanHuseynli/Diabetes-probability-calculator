point1([6, 148, 72, 35, 0, 33.6, 0.627, 50]).
point2([1, 85, 66, 29, 0, 26.6, 0.351, 31]).

euclideanDistance([], [], 0).
euclideanDistance([H1|T1], [H2|T2], Dist) :-
    euclideanDistance(T1, T2, RestDist),
    Diff is H1 - H2,
    Dist is RestDist + Diff * Diff.

main :-
    point1(P1),
    point2(P2),
    euclideanDistance(P1, P2, SumSq),
    Dist is sqrt(SumSq),
    format("Euclidean Distance: ~f~n", [Dist]).

:- initialization(main).