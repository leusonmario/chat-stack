library(nortest)
#data <- read.csv("/home/leuson/Downloads/finalOutput/general/new-askers-analysis.csv")
data <- read.csv("/home/leuson/Downloads/finalOutput/general/new-users-general-questions.csv")
subset_data_before <- data[data$account_before_chatgpt == "True", ]
subset_data_after <- data[data$account_before_chatgpt == "False", ]
print(mean(subset_data_before$number_questions))
print(mean(subset_data_after$number_questions))
shapiro_test_before <- ad.test(subset_data_before$number_questions)
shapiro_test_after <- ad.test(subset_data_after$number_questions)
print(shapiro_test_before)
print(shapiro_test_after)
wilcox_test <- wilcox.test(subset_data_before$number_questions, subset_data_after$number_questions, alternative="greater")
print(wilcox_test)


data <- read.csv("/home/leuson/Downloads/finalOutput/general/new-respondents-general-questions.csv")
subset_data_before <- data[data$account_before_chatgpt == "True", ]
subset_data_after <- data[data$account_before_chatgpt == "False", ]

#print(subset_data_before$number_questions)
print(mean(subset_data_before$number_answers))
print(mean(subset_data_after$number_answers))

shapiro_test_before <- ad.test(subset_data_before$number_answers)
shapiro_test_after <- ad.test(subset_data_after$number_answers)


print(shapiro_test_before)
print(shapiro_test_after)

wilcox_test <- wilcox.test(subset_data_before$number_answers, conf.level=0.01, subset_data_after$number_answers)

# Print the test results
print(wilcox_test)