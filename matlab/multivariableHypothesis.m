function  f  = multivariableHypothesis( n )
%UNTITLED7 Summary of this function goes here
%   
Theta = multi_sym('theta', n);
X = multi_sym('x', n);

f = real(Theta)' * real(X)

end

