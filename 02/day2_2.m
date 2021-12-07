
fpath = '/Users/emccord/code/advent_of_code/day2_input.txt';
fid = fopen(fpath);
data = textscan(fid, '%s %d');

direction = data{1};
quantity  = data{2};

horizontal = 0;
depth = 0;
aim = 0;

for inds = 1:length(direction)
   
    val = quantity(inds);
    xy = direction{inds};
    
    switch xy
        case 'forward'
            horizontal = horizontal + val;
            depth = depth + aim*val;
            
        case 'down'
            aim = aim + val;
            
        case 'up'
            aim = aim - val;
    end
    
    fprintf('Iteration %4d (dir = %7s, quant = %d, aim = %4d): x = %4d, y = %7d\n', ...
        inds, ...
        xy, ...
        val, ...
        aim, ...
        horizontal, ...
        depth);
    
end


final_answer = horizontal * depth;

disp(['Final answer = ' num2str(final_answer) '. The end.']);