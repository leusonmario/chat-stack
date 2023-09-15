file_path_no_patterns <- "/home/leuson/Downloads/finalOutput/before/generated_answers_cosine_top_score_before_no_patterns.csv"
file_path_with_patterns <- "/home/leuson/Downloads/finalOutput/before/generated_answers_cosine_top_score_before_new_patterns.csv"

# Read the CSV file
data_no_patterns <- read.csv(file_path_no_patterns)
data_with_patterns <- read.csv(file_path_with_patterns)

# Perform Shapiro-Wilk test for normality
shapiro_test_no_patterns <- shapiro.test(data_no_patterns$cosine_metric)
shapiro_test_with_patterns <- shapiro.test(data_with_patterns$cosine_metric)

print(mean(data_no_patterns$cosine_metric))
print(mean(data_with_patterns$cosine_metric))

# Print the test results
print(shapiro_test_no_patterns)
print(shapiro_test_with_patterns)

wilcox_test <- wilcox.test(data_with_patterns$cosine_metric, data_no_patterns$cosine_metric, alternative="two.sided")

# Print the test results
print(wilcox_test)

file_path_no_patterns <- "/home/leuson/Downloads/finalOutput/before/generated_answers_cosine_top_score_before_no_patterns.csv"
file_path_with_patterns <- "/home/leuson/Downloads/finalOutput/after/generated_answers_cosine_top_score_after.csv"

# Read the CSV file
data_no_patterns <- read.csv(file_path_no_patterns)
data_with_patterns <- read.csv(file_path_with_patterns)

# Perform Shapiro-Wilk test for normality
shapiro_test_no_patterns <- shapiro.test(data_no_patterns$cosine_metric)
shapiro_test_with_patterns <- shapiro.test(data_with_patterns$cosine_metric)

print(mean(data_no_patterns$cosine_metric))
print(mean(data_with_patterns$cosine_metric))

# Print the test results
print(shapiro_test_no_patterns)
print(shapiro_test_with_patterns)

wilcox_test <- wilcox.test(data_with_patterns$cosine_metric, data_no_patterns$cosine_metric, alternative="less")

# Print the test results
print(wilcox_test)

file_path_no_patterns <- "/home/leuson/Downloads/finalOutput/before/generated_answers_accepted.csv"
file_path_with_patterns <- "/home/leuson/Downloads/finalOutput/after/generated_answers_cosine.csv"

# Read the CSV file
data_no_patterns <- read.csv(file_path_no_patterns)
data_with_patterns <- read.csv(file_path_with_patterns)

# Perform Shapiro-Wilk test for normality
shapiro_test_no_patterns <- shapiro.test(data_no_patterns$cosine_metric)
shapiro_test_with_patterns <- shapiro.test(data_with_patterns$cosine_metric)

print(mean(data_no_patterns$cosine_metric))
print(sd(data_no_patterns$cosine_metric))
print(mean(data_with_patterns$cosine_metric))
print(sd(data_with_patterns$cosine_metric))

# Print the test results
print(shapiro_test_no_patterns)
print(shapiro_test_with_patterns)

wilcox_test <- wilcox.test(data_with_patterns$cosine_metric, data_no_patterns$cosine_metric, alternative="less")

# Print the test results
print(wilcox_test)