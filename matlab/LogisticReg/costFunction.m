function [ jVal, gradient ] = costFunction( theta )
%UNTITLED10 Summary of this function goes here
%   Detailed explanation goes here
jVal = sum((theta-5).^2);
gradient = 2*(theta-5);

end
