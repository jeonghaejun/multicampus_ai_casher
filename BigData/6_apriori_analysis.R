# install.packages("arules")
# install.packages("arulesViz")
library(arules)
library(arulesViz)

purchase<-read.transactions("apriori_data_id.csv",sep=",",header=TRUE)
summary(purchase)
inspect(purchase[1:10])

itemFrequency(purchase[,1:10])
itemFrequencyPlot(purchase, support=0.1)
itemFrequencyPlot(purchase, topN=10)

image(purchase[1:10])
image(sample(purchase,100))

plot(purchase)
purchaserules<-apriori(purchase, list(support=0.01, confidence=0.25, minlen=2))
purchaserules #373

summary(purchaserules)
inspect(sort(purchaserules,by=c("confidence","lift"))[1:10])

purchaserules<-sort(purchaserules,by=c("confidence","lift"))
inspect(purchaserules[1:10])

write(purchaserules, "apriori_rules.csv", sep=",", quote=FALSE, row.names=FALSE)


plot(sort(purchaserules, by = c("confidence","lift"))[1:10], method = "grouped")
plot(sort(purchaserules, by = "confidence")[1:10], method = "grouped")
plot(sort(purchaserules, by = "lift")[1:10], method = "grouped")


plot(sort(purchaserules, by = c("confidence","lift"))[1:10], method="graph", control=list(type="itemsets"),
     vertex.label.cex = 0.7,
     edge.arrow.size = 0.3,
     edge.arrow.width = 2)

plot(sort(purchaserules, by = "lift")[1:10], method="graph", control=list(type="itemsets"),
     vertex.label.cex = 0.7,
     edge.arrow.size = 0.3,
     edge.arrow.width = 2)

plot(sort(purchaserules, by = "confidence")[1:10], method="graph", control=list(type="itemsets"),
     vertex.label.cex = 0.7,
     edge.arrow.size = 0.3,
     edge.arrow.width = 2)
