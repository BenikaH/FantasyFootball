##Neeraj Asthana
##Fantasy Football Predicion
##3/23/2016
##Regression: 2015 prediction of expected points

#setup
setwd("/home/neeraj/Documents/Projects/FantasyFootball/data/formatted_data")

#read in and format ESPN predictions for 2015 season dataset and true statistics for 2015 season dataset
raw_pred <- read.csv("2015proj.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--", stringsAsFactors = FALSE)
raw_actual <- read.csv("2015stats.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--", stringsAsFactors = FALSE)  
raw_pred$PTS <- as.double(raw_pred$PTS)
raw_pred$Position <- factor(raw_pred$Position)
raw_actual$Position <- factor(raw_actual$Position)

#merge datasets so that we are able to understand them jointly
#x - 2015 prediction dataset     y - actual 2015 dataset
merging <- merge(raw_pred, raw_actual, by="Name")
dim(merging)


#QB
#Quarterbacks
qb_data <- merging[merging$Position.x == "QB",]
plot(qb_data$PTS.x,qb_data$PTS.y,col = "green", pch=19)
with(qb_data, text(PTS.y~PTS.x, labels = qb_data$Name, pos = 3, cex=.7))
