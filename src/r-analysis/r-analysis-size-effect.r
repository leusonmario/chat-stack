library(rstatix)
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/questions-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/questions-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_questions)
shapiro_test_after <- shapiro.test(data_after$number_questions)

print(mean(data_before$number_questions))
print(mean(data_after$number_questions))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions before and after")

column_name <- "number_questions"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)

#wilcox_test <- wilcox.test(data_before$number_questions, data_after$number_questions)

# Print the test results
#print(wilcox_test)

file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/answers-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/answers-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_answers)
shapiro_test_after <- shapiro.test(data_after$number_answers)

print(mean(data_before$number_answers))
print(mean(data_after$number_answers))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted answers before and after")
column_name <- "number_answers"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)


file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/comments-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/comments-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_comments)
shapiro_test_after <- shapiro.test(data_after$number_comments)

print(mean(data_before$number_comments))
print(mean(data_after$number_comments))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted comments before and after")
column_name <- "number_comments"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)

library(rstatix)
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/questions-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/one-year/questions-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_questions)
shapiro_test_after <- shapiro.test(data_after$number_questions)

print(mean(data_before$number_questions))
print(mean(data_after$number_questions))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions after and one-year")

column_name <- "number_questions"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)

#wilcox_test <- wilcox.test(data_before$number_questions, data_after$number_questions)

# Print the test results
#print(wilcox_test)

file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/answers-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/one-year/answers-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_answers)
shapiro_test_after <- shapiro.test(data_after$number_answers)

print(mean(data_before$number_answers))
print(mean(data_after$number_answers))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted answers after and one-year")
column_name <- "number_answers"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)


file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/comments-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/one-year/comments-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$number_comments)
shapiro_test_after <- shapiro.test(data_after$number_comments)

print(mean(data_before$number_comments))
print(mean(data_after$number_comments))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted comments after and one year")
column_name <- "number_comments"  # Change this if needed
if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
  stop("Column 'value' not found in one of the CSV files!")
}

# Combine datasets for independent (unpaired) test
data <- data.frame(
  value = c(data_before[[column_name]], data_after[[column_name]]),
  group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
)

# Perform Wilcoxon test
wilcox_result <- wilcox_test(data, value ~ group)

# Compute effect size
effect_size <- wilcox_effsize(data, value ~ group)

# Print results
print(wilcox_result)
print(effect_size)


