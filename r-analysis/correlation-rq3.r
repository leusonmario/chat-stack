file_path_before <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/before/reliability_before.csv"
file_path_after <- "/home/leuson/Downloads/experiment-20230927T183048Z-001/experiment/after/reliability_after.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)

#GPT

filtered_data_before_gpt <- subset(data_before, version == "chat-gpt-3.5")
filtered_data_after_gpt <- subset(data_after, version == "chat-gpt-3.5")
filtered_all_data_gpt = filtered_data_after_gpt

size_context = c()
for (x in filtered_all_data_gpt$question_description){
 size_context <- c(size_context, length(strsplit(x[1]," ")[[1]]) %/% 25)
}

print("There is a correlation between the achieved similarity and the context size given to ChatGPT - Description")
result <- cor.test(size_context, filtered_all_data_gpt$cosine_metric, method="spearman")
print(result)

size_context = c()
for (x in filtered_all_data_gpt$question_title){
 size_context <- c(size_context, length(strsplit(x[1]," ")[[1]]) %/% 2)
}

print("There is a correlation between the achieved similarity and the context size given to ChatGPT - Title")
result <- cor.test(size_context, filtered_all_data_gpt$cosine_metric, method="spearman")
print(result)

size_context = c()
for (x in filtered_all_data_gpt$tags){
 size_context <- c(size_context, length(strsplit(x, ",")[[1]]))
}

file_path <- "tags.csv"

# Export the list to a CSV file
write.csv(size_context, file = file_path, row.names = FALSE)

# Print a message to confirm the export
cat("List exported to CSV file:", file_path, "\n")

file_path <- "cosine.csv"

# Export the list to a CSV file
write.csv(filtered_all_data_gpt$cosine_metric, file = file_path, row.names = FALSE)

# Print a message to confirm the export
cat("List exported to CSV file:", file_path, "\n")

print("There is a correlation between the achieved similarity and the context size given to ChatGPT - Tags")
result <- cor.test(size_context, filtered_all_data_gpt$cosine_metric, method="spearman")
print(result)

filtered_data_before_llama <- subset(data_before, version == "llama")
filtered_data_after_llama <- subset(data_after, version == "llama")
filtered_all_data_llama = filtered_data_after_llama

size_context = c()
for (x in filtered_all_data_llama$question_description){
 size_context <- c(size_context, length(strsplit(x[1]," ")[[1]]) %/% 25)
}

print("There is a correlation between the achieved similarity and the context size given to Llama - Description")
result <- cor.test(size_context, filtered_all_data_llama$cosine_metric, method="spearman")
print(result)

size_context = c()
for (x in filtered_all_data_llama$question_title){
 size_context <- c(size_context, length(strsplit(x[1]," ")[[1]]) %/% 2)
}

print("There is a correlation between the achieved similarity and the context size given to Llama - Title")
result <- cor.test(size_context, filtered_all_data_llama$cosine_metric, method="spearman")
print(result)

size_context = c()
for (x in filtered_all_data_llama$tags){
 size_context <- c(size_context, length(strsplit(x, ",")[[1]]))
}

print("There is a correlation between the achieved similarity and the context size given to Llama - Tags")
result <- cor.test(size_context, filtered_all_data_llama$cosine_metric, method="spearman")
print(result)