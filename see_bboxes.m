load blinkerStruct.mat
for i = 1:length(blinkerStruct)
    im = imread([blinkerStruct(i).name]);
    for j = 1:length(blinkerStruct(i).bbox)
        [height, width] = size(im);
        aa = max(blinkerStruct(i).bbox(j).top+1,1);
        bb = min(blinkerStruct(i).bbox(j).top+blinkerStruct(i).bbox(j).height, height);
        cc = max(blinkerStruct(i).bbox(j).left+1,1);
        dd = min(blinkerStruct(i).bbox(j).left+blinkerStruct(i).bbox(j).width, width);
        
        imshow(im(aa:bb, cc:dd, :));
        fprintf('%d\n',blinkerStruct(i).bbox(j).label );
        pause;
    end
end