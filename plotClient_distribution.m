date='20121111Child';
distribution=strcat(date,'DIST.csv');
dist = csvread(distribution);
center=csvread(strcat(date,'CLusterCenter.csv'));
cluster=csvread(strcat(date,'cLusters.csv'));
cluster_density=csvread(strcat(date,'CLusterDensity.csv'));
j=jet;
j(1,:)=[1 1 1];
colormap(j);
imagesc((dist.^(3/4)),[0,64])
title1=strcat('Customer Distribution on ',date);
title(title1)
figure
j=jet;
j(1,:)=[1 1 1];
colormap(j);
imagesc((dist.^(3/4)),[0,64])
hold on
imagesc((cluster))
alpha scaled
plot(center(:,1),center(:,2),'*')
title2=strcat(title1,' (in clusters)');
title(title2)
figure
j=jet;
j(1,:)=[1 1 1];
colormap(j);
hold on
imagesc((cluster))
colormap(hot)
alpha scaled
plot(center(:,1),center(:,2),'*')
figure
j=jet;
j(1,:)=[1 1 1];
colormap(j);
imagesc(sqrt(cluster_density))