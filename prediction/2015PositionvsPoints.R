##Neeraj Asthana
##Fantasy Football Predicion
##Regression: 2015 draft position vs. expected number of points

#setup
setwd("/home/neeraj/Documents/Projects/FantasyFootball/data/formatted_data")
raw_data <- read.csv("2015proj.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--")
raw_data$PTS <- as.double(raw_data$PTS)

#Create a plot with a regression (marked by player position)
title <- "Draft Position vs. Expected Points"
plot(raw_data$Draft, raw_data$PTS, col = raw_data$Position, main = title, xlab = "Draft Position", ylab="Expected Points")
fit <- lm(PTS ~ Draft, data = raw_data)
abline(fit)

#Running backs
rb_data <- raw_data[raw_data$Position == "RB",]
rbfit <- lm(PTS ~ Draft, data = rb_data)
abline(rbfit, col = "blue")

#Quarterbacks
qb_data <- raw_data[raw_data$Position == "QB",]
qbfit <- lm(PTS ~ Draft, data = qb_data)
abline(qbfit, col = "green")

#Wide Receivers
wr_data <- raw_data[raw_data$Position == "WR",]
wrfit <- lm(PTS ~ Draft, data = wr_data)
abline(wrfit, col = "purple")

#TightEnds
te_data <- raw_data[raw_data$Position == "TE",]
tefit <- lm(PTS ~ Draft, data = te_data)
abline(tefit, col = "lightblue")

#Kickers
k_data <- raw_data[raw_data$Position == "K",]
kfit <- lm(PTS ~ Draft, data = k_data)
abline(kfit, col = "red")

#Defenses
df_data <- raw_data[raw_data$Position == "D/ST",]
dffit <- lm(PTS ~ Draft, data = df_data)
abline(dffit, col = "orange")