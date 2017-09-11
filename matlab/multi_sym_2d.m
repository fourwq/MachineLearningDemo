function sym_matrix = multi_sym_2d(namePrefix, m,n )
%UNTITLED9 Summary of this function goes here
%   Detailed explanation goes here
sym_matrix = sym(zeros(m,n));
for i=1:m
    for j = 1:n
         sym_matrix(i,j) = sym([namePrefix num2str(i-1) '_' num2str(j-1)]);
    end
end

end

