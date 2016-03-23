
##Neeraj Asthana
##Fantasy Football Predicion
##3/21/2016
##Regression: 2015 draft position vs. expected number of points

#setup
setwd("/home/neeraj/Documents/Projects/FantasyFootball/data/formatted_data")

#read in and formatted ESPN predictions for 2015 season
raw_data <- read.csv("2015proj.csv", header=TRUE, dec = ".", sep = ",", na.strings = "--", stringsAsFactors = FALSE)
raw_data$PTS <- as.double(raw_data$PTS)
raw_data$Position <- factor(raw_data$Position)

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



#Plots for different positions
#Runnings backs
plot(rb_data$Draft, rb_data$PTS, col="blue")
abline(rbfit, col = "blue")

#Wide Receivers
plot(wr_data$Draft, wr_data$PTS, col="purple")
abline(wrfit, col = "purple")

#Quarterbacks
qbnames = unlist(strsplit(qb_data$Name, " "))
qblast = qbnames[seq(2,length(qbnames),2)]
plot(qb_data$Draft, qb_data$PTS, col="green")
with(qb_data, text(PTS~Draft, labels = qblast, pos = 3))
abline(qbfit, col = "green")

#Tightends
tenames = unlist(strsplit(te_data$Name, " "))
telast = tenames[seq(2,length(tenames),2)]
plot(te_data$Draft, te_data$PTS, col="lightblue")
with(te_data, text(PTS~Draft, labels = telast, pos = 3))
abline(tefit, col = "lightblue")

#Defenses
plot(df_data$Draft, df_data$PTS, col="orange")
with(df_data, text(PTS~Draft, labels = df_data$Name, pos = 3))
abline(dffit, col = "orange")

#Kickers
knames = unlist(strsplit(k_data$Name, " "))
klast = knames[seq(2,length(knames),2)]
plot(k_data$Draft, k_data$PTS, col="red")
with(k_data, text(PTS~Draft, labels = klast, pos = 3))
abline(kfit, col = "red")