
fpath = '/Users/emccord/code/advent_of_code/day1_input.txt';
data = load(fpath);

three_sum = data(1:end-2) + data(2:end-1) + data(3:end);

final_answer = sum((diff(three_sum) > 0));

disp(['Final answer = ' num2str(final_answer) '. The end.']);