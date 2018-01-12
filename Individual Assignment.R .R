library ('tidyverse')
brazil <- read.csv('Brazil_data2004.csv')

colombia <- read.csv('Colombia_data2004.csv')
#

install.packages(c("maps","mapdata"))
library ('maps')
library ('mapdata')

globe <- map_data('world')

#assign the world map from the packages to a variable, to be able to use it later with $region, 
#namely the region you want to look into 

ggplot () +
  geom_polygon(data = filter (globe, globe$region == "Brazil"), mapping = aes (x=long, y = lat, group = group), fill = NA, colour = 'black') +
  geom_polygon(data = filter (globe, globe$region == "Colombia"), mapping = aes (x=long, y = lat, group = group), fill = NA, colour = 'black')+
  geom_point (data = brazil, mapping = aes(x = longitude, y = latitude), colour = 'red' ) + 
  geom_point (data = colombia, mapping = aes (x=longitude, y = latitude, colour = best))

#worked, but considering that in Brazil, there were only few deaths, and when looking at the longitude, most seeemed to have
#happened in the same city, so it just shows one red point about the deaths in Brazil 

ggplot () +
  geom_polygon(data = filter (globe, globe$region == "Brazil"), fill='white', mapping = aes (x=long, y = lat, group = group), position = "jitter", fill = NA, colour = 'black') +
  geom_point (data = brazil, mapping = aes(x = longitude, y = latitude), colour='red') 

brazil %>% filter(best > 0) %>% select(longitude, latitude, best, year)

ggplot () + 
  geom_bar(data = brazil, mapping = aes (x = best), colour = 'red') + 
  geom_bar(data=colombia, mapping = aes(x = best), colour = 'blue')


ggplot () + 
  geom_point(data = brazil, mapping = aes (x= best, y= ), colour = 'red')+
  geom_point(data=colombia, mapping = aes(x=best, y = ), colour = 'blue')
# This is a scatter plot, but it isn't very informative