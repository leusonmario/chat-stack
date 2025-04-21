# Kreppendorf alpha
#install.packages("irr")
library(irr)

print("GPT")
data <- read.csv("/home/leusonmario/postdoctoral/projects/chat-stack/data/gpt-manual-analysis-kreppendorf.csv")
data_matrix <- as.matrix(t(data[, c("manual", "gpt")]))  # Transpose the matrix
krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
print(krippendorff_alpha)

# Load CSV
data <- read.csv("/home/leusonmario/postdoctoral/projects/chat-stack/data/gpt-manual-analysis-kreppendorf.csv", stringsAsFactors = FALSE)

# Check unique values to ensure proper conversion
print(unique(c(data$manual, data$gpt)))  # Print all unique labels

# Map ordinal categories to numeric values
convert_to_numeric <- function(x) {
  if (x == "VERY HIGH") return(5)
  if (x == "HIGH") return(4)
  if (x == "MEDIUM") return(3)
  if (x == "LOW") return(2)
  if (x == "VERY LOW") return(1)
  return(NA)  # Handle unexpected values
}

# Apply conversion to manual and gpt columns
data$manual_numeric <- sapply(data$manual, convert_to_numeric)
data$gpt_numeric <- sapply(data$gpt, convert_to_numeric)

na_indices <- which(is.na(data$manual_numeric) | is.na(data$gpt_numeric))

# Print indices of NA values for manual checking
if (length(na_indices) > 0) {
  print("Rows with NA values (Check CSV file for issues):")
  print(na_indices)
  print(data[na_indices, ])  # Print the problematic rows
} else {
  print("No NA values found after conversion.")
}

# Convert to numeric matrix
data_matrix <- as.matrix(t(data[, c("manual_numeric", "gpt_numeric")]))  # Transpose the matrix

# Check for NA values before proceeding
print(sum(is.na(data_matrix)))  # If > 0, some entries were not mapped correctly

# Compute Krippendorff’s Alpha
krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
print(krippendorff_alpha)


print("LLAMA")
data <- read.csv("/home/leusonmario/postdoctoral/projects/chat-stack/data/llama-manual-analysis-kreppendorf.csv")
data_matrix <- as.matrix(t(data[, c("manual", "llama")]))  # Transpose the matrix
#krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
#print(krippendorff_alpha)

data$manual_numeric <- sapply(data$manual, convert_to_numeric)
data$gpt_numeric <- sapply(data$llama, convert_to_numeric)

# Convert to numeric matrix
data_matrix <- as.matrix(t(data[, c("manual_numeric", "gpt_numeric")]))  # Transpose the matrix

# Check for NA values before proceeding
print(sum(is.na(data_matrix)))  # If > 0, some entries were not mapped correctly

# Compute Krippendorff’s Alpha
krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
print(krippendorff_alpha)

print("GPT+LLAMA")
data <- read.csv("/home/leusonmario/postdoctoral/projects/chat-stack/data/similarity_results_combined_llama_gpt.csv")
data_matrix <- as.matrix(t(data[, c("LLAMA", "GPT")]))  # Transpose the matrix
#krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
#print(krippendorff_alpha)

data$manual_numeric <- sapply(data$LLAMA, convert_to_numeric)
data$gpt_numeric <- sapply(data$GPT, convert_to_numeric)

na_indices <- which(is.na(data$manual_numeric) | is.na(data$gpt_numeric))

# Print indices of NA values for manual checking
if (length(na_indices) > 0) {
  print("Rows with NA values (Check CSV file for issues):")
  print(na_indices)
  print(data[na_indices, ])  # Print the problematic rows
} else {
  print("No NA values found after conversion.")
}


# Convert to numeric matrix
data_matrix <- as.matrix(t(data[, c("manual_numeric", "gpt_numeric")]))  # Transpose the matrix

# Check for NA values before proceeding
print(sum(is.na(data_matrix)))  # If > 0, some entries were not mapped correctly

# Compute Krippendorff’s Alpha
krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
print(krippendorff_alpha)

print("GPT - ALL RUNS")
data <- read.csv("/home/leusonmario/postdoctoral/projects/chat-stack/data/similarity_all_runs_gpt.csv")
data_matrix <- as.matrix(t(data[, c("one", "two", "three")]))  # Transpose the matrix
#krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
#print(krippendorff_alpha)
data$one_analysis <- sapply(data$one, convert_to_numeric)
data$two_analysis <- sapply(data$two, convert_to_numeric)
data$three_analysis <- sapply(data$three, convert_to_numeric)

# Convert to numeric matrix
data_matrix <- as.matrix(t(data[, c("one_analysis", "two_analysis", "three_analysis")]))  # Transpose the matrix

# Check for NA values before proceeding
print(sum(is.na(data_matrix)))  # If > 0, some entries were not mapped correctly

# Compute Krippendorff’s Alpha
krippendorff_alpha <- kripp.alpha(data_matrix, method = "ordinal")
print(krippendorff_alpha)