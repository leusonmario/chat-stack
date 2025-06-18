# Load necessary libraries
library(ggplot2)
library(dplyr)
library(ggrepel)
library(scales)

# --- Function to read and clean data ---
read_and_clean_data <- function(file_path) {
  data <- read.csv(file_path)

  # Normalize and merge domain labels
  data_cleaned <- data %>%
    filter(!is.na(Domain) & Domain != "") %>%
    mutate(Domain = case_when(
      Domain %in% c("Tools/IDEs", "Tools/IDEs/Environment") ~ "Tools/IDEs/Environment",
      TRUE ~ Domain
    ))

  return(data_cleaned)
}

# --- File paths and corresponding model labels ---
file_paths <- c(
  "../../data/manual-analysis/Manual Analysis (Cosine) - High - GPT.csv",
  "../../data/manual-analysis/Manual Analysis (Cosine) - High - LLAMA.csv",
  "../../data/manual-analysis/Manual Analysis (Cosine) - Low - GPT.csv",
  "../../data/manual-analysis/Manual Analysis (Cosine) - Low - LLAMA.csv"
)

model_labels <- c("High Similarity (GPT)", "High Similarity (LLAMA)", "Low Similarity (GPT)", "Low Similarity (LLAMA)")

# --- Combine all domain summaries ---
combined_summary <- data.frame()

for (i in seq_along(file_paths)) {
  data_cleaned <- read_and_clean_data(file_paths[i])

  domain_summary <- data_cleaned %>%
    group_by(Domain) %>%
    summarise(count = n(), .groups = "drop") %>%
    mutate(
      percentage = count / sum(count) * 100,
      Model = model_labels[i]
    )

  combined_summary <- bind_rows(combined_summary, domain_summary)
}

# --- Define dynamic color palette for domains ---
all_domains <- sort(unique(combined_summary$Domain))
color_palette <- setNames(hue_pal()(length(all_domains)), all_domains)

# --- Create horizontal stacked bar plot ---
stacked_horizontal <- ggplot(combined_summary, aes(x = percentage, y = Model, fill = Domain)) +
  geom_bar(stat = "identity") +
  labs(
    title = "",
    x = "Percentage of Questions",
    y = "Textual Similarity by Models"
  ) +
  scale_fill_manual(values = color_palette) +
  theme_minimal(base_size = 14) +
  theme(
    legend.position = "right"
  )

# --- Save the plot ---
ggsave("domain_distribution_stacked_horizontal_barplot.png", stacked_horizontal, width = 10, height = 6)
ggsave("domain_distribution_stacked_horizontal_barplot.pdf", stacked_horizontal, width = 10, height = 6)
