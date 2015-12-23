a=csvread('20130106ClusterDensity.csv');
b=csvread('20130109ClusterDensity.csv');
center=csvread(strcat('20130106','CLusterCenter.csv'));
%center=csvread(strcat('20130227','CLusterCenter.csv'));
center_adj=[center(:,1)+20,1145-(center(:,2)+40)];
j=jet;
j(1,:)=[1 1 1];
colormap(j);
%subplot(2,1,1)
% imagesc(flipud(a))
% colorbar('Ticks',[0,1,2,3,4,5],...
%          'TickLabels',{'Empty','Very Slow','Slow','Moderate','Fast','Very Fast'})
% title('Average Pedestrian Speed in Cluster on 20121107 (Wednesday)')
% % subplot(2,1,2)
 imagesc(flipud(sqrt(a)),[0,3000])
 title('Pedestrian Distribution on 20130106 (Sunday)')
 c=colorbar
 c.Label.String = 'Square Root of Person-Time';
 %hold on
    %plot(center_adj(:,1),center_adj(:,2),'*')
 %colorbar('Ticks',[0,1,2,3,4,5],...
 %         'TickLabels',{'Empty','Very Slow','Slow','Moderate','Fast','Very Fast'})