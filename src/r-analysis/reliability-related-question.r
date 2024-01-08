file_path_no_patterns <- "/home/leuson/Downloads/finalOutput/after/analysis/analysis.csv"

# Read the CSV file
data_no_patterns <- read.csv(file_path_no_patterns)

# Perform Shapiro-Wilk test for normality
shapiro_test_no_patterns <- shapiro.test(data_no_patterns$cosine_no_support)
shapiro_test_with_patterns <- shapiro.test(data_no_patterns$cosine_support)

print(mean(data_no_patterns$cosine_no_support))
print(sd(data_no_patterns$cosine_no_support))
print(mean(data_no_patterns$cosine_support))
print(sd(data_no_patterns$cosine_support))

# Print the test results
print(shapiro_test_no_patterns)
print(shapiro_test_with_patterns)

wilcox_test <- wilcox.test(data_no_patterns$cosine_support, data_no_patterns$cosine_no_support, alternative="greater")

t_test = t.test(data_no_patterns$cosine_no_support, data_no_patterns$cosine_support, paired = TRUE)
# Print the test results
print(t_test)