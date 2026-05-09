use strict;
use warnings;
use POSIX qw(sqrt);

my @point1 = (6, 148, 72, 35, 0, 33.6, 0.627, 50);
my @point2 = (1, 85, 66, 29, 0, 26.6, 0.351, 31);

sub euclideanDistance {
    my (@p1) = @{$_[0]};
    my (@p2) = @{$_[1]};
    my $sum = 0;
    for my $i (0..$#p1) {
        $sum += ($p1[$i] - $p2[$i]) ** 2;
    }
    return sqrt($sum);
}

printf "Euclidean Distance: %.6f\n", euclideanDistance(\@point1, \@point2);