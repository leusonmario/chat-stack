library(nortest)
#data <- read.csv("/home/leuson/Downloads/finalOutput/general/new-askers-analysis.csv")
data <- read.csv("/home/leuson/Downloads/finalOutput/general/new-commentors-analysis.csv")
subset_data_before <- data[data$profile_before_chatgpt == "True", ]
subset_data_after <- data[data$profile_before_chatgpt == "False", ]

#print(subset_data_before$reputation)

shapiro_test_before <- ad.test(subset_data_before$reputation)
shapiro_test_after <- ad.test(subset_data_after$reputation)

print(mean(subset_data_before$reputation))
print(mean(subset_data_after$reputation))
print(shapiro_test_before)
print(shapiro_test_after)

wilcox_test <- wilcox.test(subset_data_before$reputation, subset_data_after$reputation, alternative="greater")

# Print the test results
print(wilcox_test)