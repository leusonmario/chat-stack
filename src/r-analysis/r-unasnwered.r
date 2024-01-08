file_path <- "/home/leuson/Downloads/finalOutput/unanswered/analysis.csv"

# Read the CSV file
data <- read.csv(file_path)

# Perform Shapiro-Wilk test for normality
shapiro_test_no_patterns <- shapiro.test(data$comments)
shapiro_test_with_patterns <- shapiro.test(data$related_question)

print(data$related_question)
print(mean(data$comments))
print(sd(data$comments))
print(mean(data$related_question))
print(sd(data$related_question))

# Print the test results
print(shapiro_test_no_patterns)
print(shapiro_test_with_patterns)

wilcox_test <- wilcox.test(data$related_question, data$comments, alternative="greater")

# Print the test results
print(wilcox_test)