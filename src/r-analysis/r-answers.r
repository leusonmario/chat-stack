library(vioplot)
library(ggplot2)
library(dplyr)

#Questions
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/questions-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/questions-analysis.csv"
file_path_year <- "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/questions-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)
data_year <- read.csv(file_path_year)

# Combine the data and add a Release column
combined_data <- rbind(data_before, data_after, data_year)
combined_data$date <- as.Date(combined_data$date)

# Update Release column to categorize dates
combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before",
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearAfter", "After"))

pdf("line-chart-questions-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_questions, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Questions Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearAfter" = "lightpink")) +  # Custom colors
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

#Answers
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/answers-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/answers-analysis.csv"
file_path_year <- "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/answers-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)
data_year <- read.csv(file_path_year)

# Combine the data and add a Release column
combined_data <- rbind(data_before, data_after, data_year)
combined_data$date <- as.Date(combined_data$date)

# Update Release column to categorize dates
combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before",
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearAfter", "After"))

pdf("line-chart-answers-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_answers, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Answers Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearAfter" = "lightpink")) +  # Custom colors
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

#Comments
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/comments-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/comments-analysis.csv"
file_path_year <- "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/comments-analysis.csv"

# Read the CSV file
data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)
data_year <- read.csv(file_path_year)

# Combine the data and add a Release column
combined_data <- rbind(data_before, data_after, data_year)
combined_data$date <- as.Date(combined_data$date)

# Update Release column to categorize dates
combined_data$Release <- ifelse(combined_data$date < as.Date("2022-11-30"), "Before",
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearAfter", "After"))

pdf("line-chart-comments-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_comments, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Comments Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearAfter" = "lightpink")) +  # Custom colors
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()
