# Load necessary libraries
library(ggplot2)
library(dplyr)
library(ggrepel)

# Read the CSV file (adjust the file path accordingly)
read_and_clean_data <- function(file_path) {
  data <- read.csv(file_path)
  data_cleaned <- data %>% filter(!is.na(Domain) & Domain != "") # Remove missing or empty domains
  return(data_cleaned)
}

# List of file paths for the four datasets
file_paths <- c("/home/leusonmario/postdoctoral/projects/chat-stack/data/manual-analysis/Manual Analysis (Cosine) - High - GPT.csv",
                "/home/leusonmario/postdoctoral/projects/chat-stack/data/manual-analysis/Manual Analysis (Cosine) - High - LLAMA.csv",
                "/home/leusonmario/postdoctoral/projects/chat-stack/data/manual-analysis/Manual Analysis (Cosine) - Low - GPT.csv",
                "/home/leusonmario/postdoctoral/projects/chat-stack/data/manual-analysis/Manual Analysis (Cosine) - Low - LLAMA.csv")
name <- c("high_GPT", "high_LLAMA", "low_GPT", "low_LLAMA")

# Create an empty list to store the cleaned data
data_list <- list()

# Initialize index for names
i <- 1

# Loop through each file, read, and clean the data
for (file in file_paths) {

  # Clean the data
  data_cleaned <- read_and_clean_data(file)

  # Summarize the data by Domain: count the number of questions in each domain
  domain_summary <- data_cleaned %>%
    group_by(Domain) %>%
    summarise(count = n()) %>%
    mutate(percentage = count / sum(count) * 100)

  # Print the summary table to see the counts and percentages
  print(domain_summary)

  # --- Create a Bar Plot for Domain Distribution using percentage ---
  ggplot(domain_summary, aes(x = Domain, y = percentage, fill = Domain)) +
  geom_bar(stat = "identity") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank())
  labs(
    title = paste("Percentage of Questions by Domain - ", name[i]),
    y = "Percentage of Questions"
  ) +
  theme_minimal()

# Save the plot as a PNG file
ggsave(paste("domain_distribution_barplot", name[i], ".png", sep = ""))

  # --- Create a Pie Chart for Domain Distribution Without Percentages ---
  domain_summary <- domain_summary %>%
  arrange(desc(Domain)) %>%
  mutate(ypos = cumsum(percentage) - (percentage / 2))  # Compute positions outside the pie

# Create the pie chart with percentage labels outside
p <- ggplot(domain_summary, aes(x = "", y = percentage, fill = Domain)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") +
  theme_void() +
  theme(legend.position = "right") +
  geom_text_repel(aes(y = ypos, label = paste0(round(percentage, 1), "%")),
                  nudge_x = 1, # Push labels outside
                  direction = "y",
                  size = 5,
                  box.padding = 0.5,
                  segment.color = "gray")

# Save the pie chart as a PDF file
ggsave(paste("domain_distribution_", name[i], ".pdf", sep = ""), plot = p, device = "pdf")

  # Increment the index for the next dataset
  i <- i + 1
}
