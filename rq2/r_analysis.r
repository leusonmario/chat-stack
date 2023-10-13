library(vioplot)

data_analysis_after = read.csv("/home/leuson/Documents/postdoctoral/LLM/Data/r_analysis_after.csv")

x1_after <- data_analysis_after$chat.gpt
x2_after <- data_analysis_after$llama

vioplot(x1_after, x2_after, names=c("chat", "llama"), col=c("gray", "light blue"))

wilcox.test(data_analysis_after$chat.gpt, data_analysis_after$llama, paired=TRUE, alternative="greater")

data_analysis_before = read.csv("/home/leuson/Documents/postdoctoral/LLM/Data/r_analysis_before.csv")

x1_before <- data_analysis_before$chat.gpt
x2_before <- data_analysis_before$llama

vioplot(x1_before, x2_before, names=c("chat", "llama"), col=c("gray", "light blue"))

wilcox.test(data_analysis_before$chat.gpt, data_analysis_before$llama, paired=TRUE, alternative="greater")

#Difference between similarity reported before and after for chatgpt
wilcox.test(data_analysis_before$chat.gpt, data_analysis_after$chat.gpt, paired=TRUE)

#Difference between similarity reported before and after for llama
wilcox.test(data_analysis_before$llama, data_analysis_after$llama, paired=TRUE)


library(rdmulti)
library(rdrobust)
library(ggplot2)
library(rdd)

release = "/home/leuson/Downloads/finalOutput/general/ddr_analysis.csv"
data = read.csv(release)

jpeg(file="questions.jpeg")
rdrobust::rdplot(y=data$number, x=data$id, c = 153, x.label="Days", y.label="Questions", title="Questions")
dev.off()

jpeg(file="questions-rdd.jpeg")
ggplot(data=data, aes(x=id, y=number)) + geom_point() + geom_smooth() + geom_vline(xintercept = 153, linetype="dotted", color = "red", linewidth=1.5)
dev.off()

sink(file="bug-reported.txt")
aux = rdrobust(y=data$number, x=data$id, c = 153)
summary(aux)
sink(file=NULL)

sink(file="question-rdd.txt")
bw <- with(data, IKbandwidth(data$id, data$number, cutpoint = 153))
rdd_simple <- RDestimate(number ~ id, data = data, cutpoint = 153, bw = bw)
summary(rdd_simple)
sink(file=NULL)