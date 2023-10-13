library(vioplot)
library(ggplot2)

#Questions
file_path_before <- "/home/leuson/Downloads/finalOutput/before/questions-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/questions-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#plotting
jpeg(file="questions-plot.jpeg")
vioplot(data_before$number_questions, data_after$number_questions,
    names=c("Before", "After"), col=c("gray", "light blue"),
    xlab = "ChatGPT Release", ylab = "Number of Questions")
dev.off()

shapiro.test(data_before$number_questions)
shapiro.test(data_after$number_questions)

#Answers
file_path_before <- "/home/leuson/Downloads/finalOutput/before/answers-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/answers-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#plotting
jpeg(file="answers-plot.jpeg")
vioplot(data_before$number_questions, data_after$number_questions,
    names=c("Before", "After"), col=c("gray", "light blue"),
    xlab = "ChatGPT Release", ylab = "Number of Answers")
dev.off()

shapiro.test(data_before$number_questions)
shapiro.test(data_after$number_questions)

#Comments
file_path_before <- "/home/leuson/Downloads/finalOutput/before/comments-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/comments-analysis.csv"


# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#plotting
jpeg(file="comments-plot.jpeg")
vioplot(data_before$number_comments, data_after$number_comments,
    names=c("Before", "After"), col=c("gray", "light blue"),
    xlab = "ChatGPT Release", ylab = "Number of Comments")
dev.off()

shapiro.test(data_before$number_comments)
shapiro.test(data_after$number_comments)

#Similarity
file_path_before <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/before/reliability_before.csv"
file_path_after <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/after/reliability_after.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#GPT

filtered_data_before_gpt <- subset(data_before, version == "chat-gpt-3.5")
filtered_data_after_gpt <- subset(data_after, version == "chat-gpt-3.5")
filtered_all_data_gpt = mapply(c, filtered_data_before_gpt, filtered_data_after_gpt, SIMPLIFY=FALSE)

mean_before = mean(filtered_data_before_gpt$cosine_metric)
mean_after = mean(filtered_data_after_gpt$cosine_metric)

print("Mean before - GPT")
print(mean_before)
print("Mean after - GPT")
print(mean_after)

print("Normality - Before GPT")
normality_before = shapiro.test(filtered_data_before_gpt$cosine_metric)
print(normality_before)
print("Normality - After GPT")
normality_after = shapiro.test(filtered_data_after_gpt$cosine_metric)
print(normality_after)
print("Normality - All GPT")
normality_all = shapiro.test(filtered_all_data_gpt$cosine_metric)
print(normality_all)

aux_gpt = wilcox.test(filtered_data_after_gpt$cosine_metric, filtered_data_before_gpt$cosine_metric, paired=FALSE)

print("Wilcoxon Test - GPT")
print("There is no difference regarding the achieved similarity before and after GPT release for ChatGPT")
print(aux_gpt)

size_context = c()
for (x in filtered_all_data_gpt$tags){
 size_context <- c(size_context, length(strsplit(x, ",")[[1]]))
 # print(length(strsplit(x, ",")[[1]]))
}

print("There is a correlation between the achieved similarity and the context size given to ChatGPT")
result <- cor.test(filtered_all_data_gpt$cosine_metric, size_context, method="spearman")
print(result)

#plotting
jpeg(file="similarity-plot-gpt.jpeg")
vioplot(filtered_data_before_gpt$cosine_metric, filtered_data_after_gpt$cosine_metric,
    names=c("Before", "After"), col=c("gray", "light blue"),
    xlab = "ChatGPT Release", ylab = "Cosine Similarity")
dev.off()

#Llama
filtered_data_before_llama <- subset(data_before, version == "llama")
filtered_data_after_llama <- subset(data_after, version == "llama")
filtered_all_data_llama = mapply(c, filtered_data_before_llama, filtered_data_after_llama, SIMPLIFY=FALSE)

mean_before = mean(filtered_data_before_llama$cosine_metric)
mean_after = mean(filtered_data_after_llama$cosine_metric)

print("Mean before - Llama")
print(mean_before)
print("Mean after - Llama")
print(mean_after)

print("Normality - Before Llama")
normality_before = shapiro.test(filtered_data_before_llama$cosine_metric)
print(normality_before)
print("Normality - After Llama")
normality_after = shapiro.test(filtered_data_after_llama$cosine_metric)
print(normality_after)
print("Normality - All Llama")
normality_all = shapiro.test(filtered_all_data_llama$cosine_metric)
print(normality_all)

aux_llama = wilcox.test(filtered_data_after_llama$cosine_metric, filtered_data_before_llama$cosine_metric, paired=FALSE)
print("Wilcoxon Test - Llama")
print("There is no difference regarding the achieved similarity before and after GPT release for Llama")
print(aux_llama)

#plotting
jpeg(file="similarity-plot-llama.jpeg")
vioplot(filtered_data_before_llama$cosine_metric, filtered_data_after_llama$cosine_metric,
    names=c("Before", "After"), col=c("gray", "light blue"),
    xlab = "ChatGPT Release", ylab = "Cosine Similarity") + theme(axis.title.x = element_text(size = 16))
dev.off()

print("Wilcoxon Test - Llama and GPT")
print("There is no difference regarding the achieved similarity between ChatGPT and Llama")
aux_llama_gpt = wilcox.test(filtered_all_data_gpt$cosine_metric, filtered_all_data_llama$cosine_metric, paired=TRUE, alternative="greater")
print(aux_llama_gpt)

size_context = c()
for (x in filtered_all_data_gpt$tags){
 size_context <- c(size_context, length(strsplit(x, ",")[[1]]))
}

result <- cor.test(filtered_all_data_llama$cosine_metric, size_context, method="spearman")
print(result)