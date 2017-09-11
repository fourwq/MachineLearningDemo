X = (1:3)';
y = (1:3)'+2;
theta = [0;1];
cost = costFunctionJ(X,y,theta);
disp(cost)


