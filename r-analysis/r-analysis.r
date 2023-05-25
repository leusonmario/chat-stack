file_path_before <- "/home/leuson/Downloads/finalOutput/before/questions-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/questions-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
#shapiro_test_before <- shapiro.test(data_before$number_questions)
#shapiro_test_after <- shapiro.test(data_after$number_questions)

print(mean(data_before$number_questions))
print(mean(data_after$number_questions))

# Print the test results
#print(shapiro_test_before)
#print(shapiro_test_after)

wilcox_test <- wilcox.test(data_before$number_questions, data_after$number_questions, , alternative="greater")

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/finalOutput/before/answers-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/answers-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
#shapiro_test_before <- shapiro.test(data_before$number_questions)
#shapiro_test_after <- shapiro.test(data_after$number_questions)

print(mean(data_before$number_questions))
print(mean(data_after$number_questions))

# Print the test results
#print(shapiro_test_before)
#print(shapiro_test_after)

wilcox_test <- wilcox.test(data_before$number_questions, data_after$number_questions, alternative="greater")

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/finalOutput/before/comments-analysis.csv"
file_path_after <- "/home/leuson/Downloads/finalOutput/after/comments-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
#shapiro_test_before <- shapiro.test(data_before$number_questions)
#shapiro_test_after <- shapiro.test(data_after$number_questions)

print(mean(data_before$number_comments))
print(mean(data_after$number_comments))

# Print the test results
#print(shapiro_test_before)
#print(shapiro_test_after)

wilcox_test <- wilcox.test(data_before$number_comments, data_after$number_comments, alternative="greater")

# Print the test results
print(wilcox_test)