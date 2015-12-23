date_pool=['20121024','20121028','20121031','20121104','20121107','20121111','20121114','20121118','20121121','20121125','20121128','20121202','20121205','20121209','20121212','20121216','20121219','20121223','20121226','20130106','20130109','20130113','20130116','20130120','20130123','20130127','20130130','20130203','20130206','20130210','20130213','20130217','20130220','20130224','20130227','20130303','20130306','20130310','20130317','20130320','20130324','20130327'];
Week_pool={' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Wednesday',' Sunday',' Sunday',' Wednesday',' Sunday',' Wednesday'};
j=jet;
j(1,:)=[1 1 1];
colormap(j);
for i=0:41
    date=date_pool((i*8+1):(i*8+8));
    date
    distribution=strcat(date,'DIST.csv');
    dist = flipud(csvread(distribution));
    center=flipud(csvread(strcat(date,'CLusterCenter.csv')));
    cluster=flipud(csvread(strcat(date,'CLusters.csv')));
    cluster_density=flipud(csvread(strcat(date,'CLusterDensity.csv')));
    imagesc((dist.^(3/4)),[0,64]);
    title1=strcat('Customer Distribution on 2',date(2:end),Week_pool(i+1));
    title(title1)
    drawnow
    frame = getframe(1);
    im = frame2im(frame);
    [A,map] = rgb2ind(im,256); 
    if(i==0)
        imwrite(A,map,'1clientDistribution.gif','DelayTime',0.5,'LoopCount',Inf)
    else
        imwrite(A,map,'1clientDistribution.gif','WriteMode','append','DelayTime',0.5)    
    end
    
end