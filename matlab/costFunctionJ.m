function cost = costFunctionJ(X,y,theta)
% ??hypothesis??h(x) = theta0 +theta1*x1
numOfDataSample = size(X,1);
X = [ones(numOfDataSample,1), X];
h_x = X*theta;
cost = sum((h_x-y).^2)/(2*numOfDataSample);

end