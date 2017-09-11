function sym_matrix = multi_sym(namePrefix, n)
%UNTITLED8 Summary of this function goes here
%   generate column vector

sym_matrix = sym(zeros(n,1));
for i=1:n
    sym_matrix(i,1) = sym([namePrefix num2str(i-1)]);
end

end

