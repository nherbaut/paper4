#define output file for plot
pdf(file="output.pdf")

#Load time serie library
library("xts")
library("forecast")
fc_len<-50

#generate test data or use real trace from IXP
#create a new experiment 
system("python main2.py > simu.csv")
v<-read.csv(file="simu.csv",header=FALSE)
#read simulation file
#v<-read.csv(file="test2.csv",header=FALSE)
#create variables from the data
#unpack list to vector
v2<-unlist(v["V2"])
v1<-unlist(v["V1"])
#convert vector from string to date
v1<-as.POSIXct(v1)
#create the time serie object we fit
data<-ts(v2[1:(length(v1)-fc_len)],frequency=24)
#automatically fit sarima
m<-auto.arima(data)
print(m)
#save plot to pdf file
fc<-forecast(m,level=c(95,80),fc_len)
#display predictions
plot(append(coredata(fc$x),fc$mean),type="l",col="blue",pch=22, lty=2)
#display original data
lines(coredata(v2),col="black",lwd=2)


