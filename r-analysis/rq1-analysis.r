library(vioplot)
library(ggplot2)
library(dplyr)

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

merged_data <- rbind(data_before, data_after)

data1 <- data_before
data2 <- data_after

data2$group <- "After"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1)
custom_colors <- c("After" = "light blue", " Before" = "gray")


pdf("questions-plot2.pdf")
ggplot(combined_data, aes(x = group, y = number_questions, fill = group)) +
  geom_violin(scale = "width", trim=FALSE) +
  scale_y_continuous(name = "Number of Questions") +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 16))
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

data1 <- data_before
data2 <- data_after

data2$group <- "After"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1)
custom_colors <- c("After" = "light blue", " Before" = "gray")


pdf("answers-plot2.pdf")
ggplot(combined_data, aes(x = group, y = number_questions, fill = group)) +
  geom_violin(scale = "width", trim=FALSE) +
  scale_y_continuous(name = "Number of Answers") +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 16))
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

data1 <- data_before
data2 <- data_after

data2$group <- "After"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1)
custom_colors <- c("After" = "light blue", " Before" = "gray")


pdf("comments-plot2.pdf")
ggplot(combined_data, aes(x = group, y = number_comments, fill = group)) +
  geom_violin(scale = "width", trim=FALSE) +
  scale_y_continuous(name = "Number of Comments") +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text.y = element_text(margin = margin(r = 45))) +
  theme(axis.text = element_text(size = 16))
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

data1 <- filtered_data_before_gpt
data2 <- filtered_data_after_gpt

data2$group <- "After"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1)
custom_colors <- c("After" = "light blue", " Before" = "gray")


pdf(file="similarity-plot-gpt2.pdf")
ggplot(combined_data, aes(x = group, y = cosine_metric, fill = group)) +
  geom_violin(scale = "width", trim=FALSE) +
  scale_y_continuous(name = "Cosine Similarity") +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text.y = element_text(margin = margin(r = 45))) +
  theme(axis.text = element_text(size = 25))
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
    xlab = "ChatGPT Release", ylab = "Cosine Similarity") + theme(axis.title.x = element_text(size = 16)) +
    theme(axis.text = element_text(size = 12))
dev.off()

data1 <- filtered_data_before_llama
data2 <- filtered_data_after_llama

data2$group <- "After"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1)
custom_colors <- c("After" = "light blue", " Before" = "gray")


pdf(file="similarity-plot-llama2.pdf")
ggplot(combined_data, aes(x = group, y = cosine_metric, fill = group)) +
  geom_violin(scale = "width", trim=FALSE) +
  scale_y_continuous(name = "Cosine Similarity") +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text.y = element_text(margin = margin(r = 45))) +
  theme(axis.text = element_text(size = 25))
dev.off()

print("MEAN - GPT - ALL")
print(mean(filtered_all_data_gpt$cosine_metric))
print("MEAN - LLAMA - ALL")
print(mean(filtered_all_data_llama$cosine_metric))

print("Wilcoxon Test - Llama and GPT")
print("There is no difference regarding the achieved similarity between ChatGPT and Llama")
aux_llama_gpt = wilcox.test(filtered_all_data_gpt$cosine_metric, filtered_all_data_llama$cosine_metric, paired=TRUE, alternative="greater")
print(aux_llama_gpt)

library(effsize)
delta <- cliff.delta(filtered_all_data_gpt$cosine_metric, filtered_all_data_llama$cosine_metric)
print(delta)

size_context = c()
for (x in filtered_all_data_gpt$tags){
 size_context <- c(size_context, length(strsplit(x, ",")[[1]]))
}

result <- cor.test(filtered_all_data_llama$cosine_metric, size_context, method="spearman")
print(result)


data1 <- read.csv("/home/leuson/Downloads/ResultsFinal/after/questions-analysis.csv", stringsAsFactors = FALSE)
data2 <- read.csv("/home/leuson/Downloads/ResultsFinal/before/questions-analysis.csv", stringsAsFactors = FALSE)

combined_data <- rbind(data1, data2)
combined_data$date <- as.Date(combined_data$date)

combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before", "After")

pdf("line-chart-questions-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_questions, color = Release)) +
  geom_line(size = 1) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  labs(title = "Number of Questions Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue")) +
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

data1 <- read.csv("/home/leuson/Downloads/ResultsFinal/after/answers-analysis.csv", stringsAsFactors = FALSE)
data2 <- read.csv("/home/leuson/Downloads/ResultsFinal/before/answers-analysis.csv", stringsAsFactors = FALSE)

combined_data <- rbind(data1, data2)
combined_data$date <- as.Date(combined_data$date)

combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before", "After")

pdf("line-chart-answers-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_answers, color = Release)) +
  geom_line(size = 1) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  labs(title = "Number of Answers Over Time", x = "Date", y="") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue")) +
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

data1 <- read.csv("/home/leuson/Downloads/ResultsFinal/after/comments-analysis.csv", stringsAsFactors = FALSE)
data2 <- read.csv("/home/leuson/Downloads/ResultsFinal/before/comments-analysis.csv", stringsAsFactors = FALSE)

combined_data <- rbind(data1, data2)
combined_data$date <- as.Date(combined_data$date)

combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before", "After")

pdf("line-chart-comments-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_comments, color = Release)) +
  geom_line(size = 1) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  labs(title = "Number of Comments Over Time", x = "Date", y="") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue")) +
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

# Kreppendorf alpha
library(irr)

print("GPT")
data <- read.csv("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/gpt-manual-analysis-kreppendorf.csv")
data_matrix <- as.matrix(t(data[, c("manual", "gpt")]))  # Transpose the matrix
krippendorff_alpha <- kripp.alpha(data_matrix, method = "nominal")
print(krippendorff_alpha)

print("LLAMA")
data <- read.csv("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/llama-manual-analysis-kreppendorf.csv")
data_matrix <- as.matrix(t(data[, c("manual", "llama")]))  # Transpose the matrix
krippendorff_alpha <- kripp.alpha(data_matrix, method = "nominal")
print(krippendorff_alpha)

print("GPT+LLAMA")
data <- read.csv("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity_results_combined_llama_gpt.csv")
data_matrix <- as.matrix(t(data[, c("LLAMA", "GPT")]))  # Transpose the matrix
krippendorff_alpha <- kripp.alpha(data_matrix, method = "nominal")
print(krippendorff_alpha)

print("GPT - ALL RUNS")
data <- read.csv("/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/similarity_all_runs_gpt.csv")
data_matrix <- as.matrix(t(data[, c("one", "two", "tree")]))  # Transpose the matrix
krippendorff_alpha <- kripp.alpha(data_matrix, method = "nominal")
print(krippendorff_alpha)