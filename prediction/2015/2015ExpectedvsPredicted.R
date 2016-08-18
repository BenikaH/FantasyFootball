##Neeraj Asthana
##Fantasy Football Predicion
##3/22/2016
##Regression: 2015 draft position vs. expected number of points

#setup
setwd("/home/neeraj/Documents/Projects/FantasyFootball/data/formatted")

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

#Regression of Expected vs. Actual
fit <- lm(PTS.y ~ PTS.x - 1,data=merging)
title <- "2015 Actual Points Scored vs. Predicted Points"
xlabel <- "Predicted Points"
ylabel <- "Actual Points"
plot(PTS.y ~ PTS.x, col = Position.x, data=merging, main = title, xlab = xlabel, ylab = ylabel)
abline(0,1, col="orange") #above this line is an overperformer and below is an underperformer
abline(fit, col = "yellow")


#Running backs
rb_data <- merging[merging$Position.y == "RB",]
rbfit <- lm(PTS.y ~ PTS.x - 1, data = rb_data)
rbfit2 <- lm(PTS.y ~ PTS.x, data = rb_data)
abline(rbfit, col = "blue")

#Quarterbacks
qb_data <- merging[merging$Position.y == "QB",]
qbfit <- lm(PTS.y ~ PTS.x - 1, data = qb_data)
qbfit2 <- lm(PTS.y ~ PTS.x, data = qb_data)
abline(qbfit, col = "green")

#Wide Receivers
wr_data <- merging[merging$Position.y == "WR",]
wrfit <- lm(PTS.y ~ PTS.x - 1, data = wr_data)
wrfit2 <- lm(PTS.y ~ PTS.x, data = wr_data)
abline(wrfit, col = "purple")

#TightEnds
te_data <- merging[merging$Position.y == "TE",]
tefit <- lm(PTS.y ~ PTS.x - 1, data = te_data)
tefit2 <- lm(PTS.y ~ PTS.x, data = te_data)
abline(tefit, col = "lightblue")

#Kickers
k_data <- merging[merging$Position.y == "K",]
kfit <- lm(PTS.y ~ PTS.x - 1, data = k_data)
kfit2 <- lm(PTS.y ~ PTS.x, data = k_data)
abline(kfit, col = "red")

#Defenses
df_data <- merging[merging$Position.y == "D/ST",]
dffit <- lm(PTS.y ~ PTS.x - 1, data = df_data)
dffit2 <- lm(PTS.y ~ PTS.x, data = df_data)
abline(dffit, col = "black")



#Plots for different positions
#Runnings backs
rbnames = strsplit(rb_data$Name, " ")
rblast = c()
for(p in rbnames){
  rblast <- c(rblast, p[2])
}
plot(rb_data$PTS.x, rb_data$PTS.y, col="blue", xlab= xlabel, ylab=ylabel)
with(rb_data, text(PTS.y~PTS.x, labels = rblast, pos = 3))
abline(0,1, col="orange") #above this line is an overperformer and below is an underperformer
abline(rbfit, col = "blue")

#Wide Receivers
plot(wr_data$Draft, wr_data$PTS, col="purple")
abline(wrfit, col = "purple")

#Quarterbacks
qbnames = unlist(strsplit(qb_data$Name, " "))
qblast = qbnames[seq(2,length(qbnames),2)]
plot(qb_data$PTS.x, qb_data$PTS.y, col="green", xlab=xlabel, ylab = ylabel)
with(qb_data, text(PTS.y~PTS.x, labels = qblast, pos = 3))
abline(0,1, col="orange") #above this line is an overperformer and below is an underperformer
abline(qbfit, col = "green")
abline(qbfit2, col = "green", lty=2)

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