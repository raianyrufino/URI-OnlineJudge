A,B,C,D = map(int,raw_input().split())
if (A<B+C and B<A+C and C<B+A) or (A<D+C and D<A+C and C<D+A) or (A<B+D and B<A+D and D<B+A) or (D<B+C and B<D+C and C<B+D):
  print "S"
else:
  print "N"
