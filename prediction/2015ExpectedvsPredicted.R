##Neeraj Asthana
##Fantasy Football Predicion
##3/22/2016
##Regression: 2015 draft position vs. expected number of points

#setup
setwd("/home/neeraj/Documents/Projects/FantasyFootball/data/formatted_data")

#read in and format ESPN predictions for 2015 season dataset and true statistics for 2015 season dataset
raw_pred_data <- read.csv("2015proj.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--", stringsAsFactors = FALSE)
raw_actual_data <- read.csv("2015stats.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--", stringsAsFactors = FALSE)  
raw_pred_data$PTS <- as.double(raw_pred_data$PTS)
raw_pred_data$Position <- factor(raw_pred_data$Position)
raw_actual_data$Position <- factor(raw_actual_data$Position)