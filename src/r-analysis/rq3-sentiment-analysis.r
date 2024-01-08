library(vioplot)

file_path_before <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/sentiment-analysis-before-new.csv"
file_path_after <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/sentiment-analysis-after-new.csv"

data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#GPT

filtered_data_before_positive_gpt <- subset(data_before, model == "chat-gpt-3.5" & label == "positive")
filtered_data_before_negative_gpt <- subset(data_before, model == "chat-gpt-3.5" & label == "negative")
filtered_data_before_neutral_gpt <- subset(data_before, model == "chat-gpt-3.5" & label == "neutral")
filtered_data_after_positive_gpt <- subset(data_after, model == "chat-gpt-3.5" & label == "positive")
filtered_data_after_negative_gpt <- subset(data_after, model == "chat-gpt-3.5" & label == "negative")
filtered_data_after_neutral_gpt <- subset(data_after, model == "chat-gpt-3.5" & label == "neutral")

filtered_all_data_positive_gpt = rbind(filtered_data_before_positive_gpt, filtered_data_after_positive_gpt)
filtered_all_data_negative_gpt = rbind(filtered_data_before_negative_gpt, filtered_data_after_negative_gpt)
filtered_all_data_neutral_gpt = rbind(filtered_data_before_neutral_gpt, filtered_data_after_neutral_gpt)

filtered_all_data_gpt = rbind(filtered_data_before_positive_gpt, filtered_data_after_positive_gpt,
filtered_data_before_negative_gpt, filtered_data_after_negative_gpt,filtered_data_after_neutral_gpt,
filtered_data_before_neutral_gpt)

print("GPT - POSITIVE")
length(filtered_all_data_positive_gpt$score)
print("GPT - NEGATIVE")
length(filtered_all_data_negative_gpt$score)
print("GPT - NEUTRAL")
length(filtered_all_data_neutral_gpt$score)
#shapiro.test(filtered_all_data_negative_gpt$score)

#LLAMA

filtered_data_before_positive_llama <- subset(data_before, model == "llama" & label == "positive")
filtered_data_before_negative_llama <- subset(data_before, model == "llama" & label == "negative")
filtered_data_before_neutral_llama <- subset(data_before, model == "llama" & label == "neutral")
filtered_data_after_positive_llama <- subset(data_after, model == "llama" & label == "positive")
filtered_data_after_negative_llama <- subset(data_after, model == "llama" & label == "negative")
filtered_data_after_neutral_llama <- subset(data_after, model == "llama" & label == "neutral")

filtered_all_data_positive_llama = rbind(filtered_data_before_positive_llama, filtered_data_after_positive_llama)
filtered_all_data_negative_llama = rbind(filtered_data_before_negative_llama, filtered_data_after_negative_llama)
filtered_all_data_neutral_llama = rbind(filtered_data_before_neutral_llama, filtered_data_after_neutral_llama)

filtered_all_data_llama = rbind(filtered_data_before_positive_llama, filtered_data_after_positive_llama,
filtered_data_before_negative_llama, filtered_data_after_negative_llama, filtered_data_before_neutral_llama,
filtered_data_after_neutral_llama)

print("LLAMA - POSITIVE")
length(filtered_all_data_positive_llama$score)
print("LLAMA - NEGATIVE")
length(filtered_all_data_negative_llama$score)
print("LLAMA - NEUTRAL")
length(filtered_all_data_neutral_llama$score)
#shapiro.test(filtered_all_data_negative_llama$score)


#ORIGINAL
filtered_data_before_positive_original <- subset(data_before, model == "original-answer" & label == "positive")
filtered_data_before_negative_original <- subset(data_before, model == "original-answer" & label == "negative")
filtered_data_before_neutral_original <- subset(data_before, model == "original-answer" & label == "neutral")
filtered_data_after_positive_original <- subset(data_after, model == "original-answer" & label == "positive")
filtered_data_after_negative_original <- subset(data_after, model == "original-answer" & label == "negative")
filtered_data_after_neutral_original <- subset(data_after, model == "original-answer" & label == "neutral")

filtered_all_data_positive_original = rbind(filtered_data_before_positive_original, filtered_data_after_positive_original)
filtered_all_data_negative_original = rbind(filtered_data_before_negative_original, filtered_data_after_negative_original)
filtered_all_data_neutral_original = rbind(filtered_data_before_neutral_original, filtered_data_after_neutral_original)

filtered_all_data_original = rbind(filtered_data_before_positive_original, filtered_data_after_positive_original,
filtered_data_before_negative_original, filtered_data_after_negative_original,filtered_data_before_neutral_original,
filtered_data_after_neutral_original)

print("ORIGINAL - ORIGINAL")
length(filtered_all_data_positive_original$score)
print("ORIGINAL - NEGATIVE")
length(filtered_all_data_negative_original$score)
print("ORIGINAL - NEUTRAL")
length(filtered_all_data_neutral_original$score)
shapiro.test(filtered_all_data_negative_original$score)

length(rbind(filtered_all_data_positive_gpt, filtered_all_data_positive_llama, filtered_all_data_positive_original)$score)
length(rbind(filtered_all_data_negative_gpt, filtered_all_data_negative_llama, filtered_all_data_negative_original)$score)

#NEUTRAL
#GPT/LLAMA
wilcox.test(filtered_all_data_neutral_gpt$score, filtered_all_data_neutral_llama$score, alternative="greater")
#GPT/ORIGINAL
wilcox.test(filtered_all_data_neutral_gpt$score, filtered_all_data_neutral_original$score, alternative="greater")
#LLAMA/ORIGINAL
wilcox.test(filtered_all_data_neutral_original$score, filtered_all_data_neutral_llama$score, alternative="greater")
