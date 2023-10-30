file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/questions-analysis.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/questions-analysis.csv"

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
wilcox_test <- wilcox.test(data_before$number_questions, data_after$number_questions)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/answers-analysis.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/answers-analysis.csv"

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
wilcox_test <- wilcox.test(data_before$number_answers, data_after$number_answers)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/comments-analysis.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/comments-analysis.csv"

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
wilcox_test <- wilcox.test(data_before$number_comments, data_after$number_comments)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/python-tag.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/python-tag.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$value)
shapiro_test_after <- shapiro.test(data_after$value)

print(sum(data_before$value))
print(sum(data_after$value))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions with the tag python")
wilcox_test <- wilcox.test(data_before$value, data_after$value)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/javascript-tag.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/javascript-tag.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$value)
shapiro_test_after <- shapiro.test(data_after$value)

print(sum(data_before$value))
print(sum(data_after$value))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions with the tag javascript")
wilcox_test <- wilcox.test(data_before$value, data_after$value)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/reactjs-tag.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/reactjs-tag.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$value)
shapiro_test_after <- shapiro.test(data_after$value)

print(sum(data_before$value))
print(sum(data_after$value))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions with the tag reactjs")
wilcox_test <- wilcox.test(data_before$value, data_after$value)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/java-tag.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/java-tag.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$value)
shapiro_test_after <- shapiro.test(data_after$value)

print(sum(data_before$value))
print(sum(data_after$value))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions with the tag java")
wilcox_test <- wilcox.test(data_before$value, data_after$value)

# Print the test results
print(wilcox_test)

file_path_before <- "/home/leuson/Downloads/ResultsFinal/before/c#-tag.csv"
file_path_after <- "/home/leuson/Downloads/ResultsFinal/after/c#-tag.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

# Perform Shapiro-Wilk test for normality
shapiro_test_before <- shapiro.test(data_before$value)
shapiro_test_after <- shapiro.test(data_after$value)

print(sum(data_before$value))
print(sum(data_after$value))

# Print the test results
print(shapiro_test_before)
print(shapiro_test_after)

print("Difference between the number of posted questions with the tag c#")
wilcox_test <- wilcox.test(data_before$value, data_after$value)

# Print the test results
print(wilcox_test)