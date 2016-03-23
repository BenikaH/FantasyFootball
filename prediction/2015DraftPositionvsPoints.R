##Neeraj Asthana
##Fantasy Football Predicion
##3/23/2016
##Regression: 2015 draft position vs. points scored

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

#Create a plot with a regression (marked by player position)
title <- "Draft Position vs. Points Scored"
plot(merging$Draft, merging$PTS.y+merging$REC.y, col = merging$Position.x, main = title, xlab = "Draft Position", ylab="Points Scored", pch=19)
with(merging, text((PTS.y + REC.y)~Draft, labels = merging$Name, pos = 3, cex=.5))
#legend("topright", legend=unique(merging$Position.x), col = c("red", "purple", "blue", "black", "green", "lightblue"))

fit <- lm(PTS ~ Draft, data = raw_data)
abline(fit)