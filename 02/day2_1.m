
fpath = '/Users/emccord/code/advent_of_code/day2_input.txt';
fid = fopen(fpath);
data = textscan(fid, '%s %d');

forward_inds = strcmp(data{1}, 'forward');
down_inds = strcmp(data{1}, 'down');
up_inds = strcmp(data{1}, 'up');

forward_sum = sum(data{2}(forward_inds));
up_sum = sum(data{2}(up_inds));
down_sum = sum(data{2}(down_inds));

y_diff = down_sum - up_sum;

final_answer = forward_sum * y_diff;

disp(['Final answer = ' num2str(final_answer) '. The end.']);