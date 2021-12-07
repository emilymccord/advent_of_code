
fpath = '/Users/emccord/code/advent_of_code/day1_input.txt';
data = load(fpath);

final_answer = sum((diff(data) > 0));

disp(['Final answer = ' num2str(final_answer) '. The end.']);