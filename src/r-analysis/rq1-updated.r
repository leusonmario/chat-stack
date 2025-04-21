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

min_value <- min(c(data_before$number_questions, data_after$number_questions, data_year$number_questions), na.rm = TRUE)
max_value <- max(c(data_before$number_questions, data_after$number_questions, data_year$number_questions), na.rm = TRUE)

#plotting
jpeg(file="questions-plot.jpeg")
vioplot(data_before$number_questions, data_after$number_questions, data_year$number_questions,
    names=c("Before", "After", "OneYear"), col=c("gray", "light blue", "green"),
    xlab = "ChatGPT Release", ylab = "Number of Questions")
dev.off()

merged_data <- rbind(data_before, data_after, data_year)

data1 <- data_before
data2 <- data_after
data3 <- data_year

data2$group <- "After"
data3$group <- "OneYearMilestone"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1, data3)
custom_colors <- c("After" = "light blue", " Before" = "gray", "OneYearMilestone" = "lightpink")

# Calculate the common y-axis range
min_value <- min(combined_data$number_questions, na.rm = TRUE)
max_value <- max(combined_data$number_questions, na.rm = TRUE)

pdf("questions-plot2.pdf", width = 10, height = 8)
ggplot(combined_data, aes(x = group, y = number_questions, fill = group)) +
  geom_violin(trim = FALSE) +
  scale_y_continuous(name = "Number of Questions", limits = c(min_value, max_value)) +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 16))
dev.off()

shapiro.test(data_before$number_questions)
shapiro.test(data_after$number_questions)

#Answers
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/answers-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/answers-analysis.csv"
file_path_year <- "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/answers-analysis.csv"

data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)
data_year <- read.csv(file_path_year)

min_value <- min(c(data_before$number_answers, data_after$number_answers, data_year$number_answers), na.rm = TRUE)
max_value <- max(c(data_before$number_answers, data_after$number_answers, data_year$number_answers), na.rm = TRUE)

#plotting
jpeg(file="answers-plot.jpeg")
vioplot(data_before$number_answers, data_after$number_answers, data_year$number_answers,
    names=c("Before", "After", "OneYear"), col=c("gray", "light blue", "light green"),
    xlab = "ChatGPT Release", ylab = "Number of Answers")
dev.off()

merged_data <- rbind(data_before, data_after, data_year)

data1 <- data_before
data2 <- data_after
data3 <- data_year

data2$group <- "After"
data3$group <- "OneYearMilestone"
data1$group <- " Before"

combined_data <- bind_rows(data2, data1, data3)
custom_colors <- c("After" = "light blue", " Before" = "gray", "OneYearMilestone" = "lightpink")

# Calculate the common y-axis range
min_value <- min(combined_data$number_answers, na.rm = TRUE)
max_value <- max(combined_data$number_answers, na.rm = TRUE)

pdf("answers-plot2.pdf", width = 10, height = 8)
ggplot(combined_data, aes(x = group, y = number_answers, fill = group)) +
  geom_violin(trim = FALSE) +
  scale_y_continuous(name = "Number of Answers", limits = c(min_value, max_value)) +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 16))
dev.off()

shapiro.test(data_before$number_answers)
shapiro.test(data_after$number_answers)

#Comments
file_path_before <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/before/comments-analysis.csv"
file_path_after <- "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/comments-analysis.csv"
file_path_year <- "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/comments-analysis.csv"

data_before <- read.csv(file_path_before)
data_after <- read.csv(file_path_after)
data_year <- read.csv(file_path_year)

min_value <- min(c(data_before$number_comments, data_after$number_comments, data_year$number_comments), na.rm = TRUE)
max_value <- max(c(data_before$number_comments, data_after$number_comments, data_year$number_comments), na.rm = TRUE)


#plotting
jpeg(file="comments-plot.jpeg")
vioplot(data_before$number_comments, data_after$number_comments, data_year$number_comments,
    names=c("Before", "After", "OneYear"), col=c("gray", "light blue", "light green"),
    xlab = "ChatGPT Release", ylab = "Number of Comments")
dev.off()

data1 <- data_before
data2 <- data_after
data3 <- data_year

data2$group <- "After"
data1$group <- " Before"
data3$group <- "OneYearMilestone"

combined_data <- bind_rows(data2, data1, data3)
custom_colors <- c("After" = "light blue", " Before" = "gray", "OneYearMilestone" = "lightpink")

pdf("comments-plot2.pdf", width = 10, height = 8)#, height = 6)  # Adjust width if necessary
ggplot(combined_data, aes(x = group, y = number_comments, fill = group)) +
  geom_violin(trim = FALSE) +
  scale_y_continuous(name = "Number of Comments", limits = c(min_value, max_value)) +
  facet_wrap(~group, scales = "free") +
  theme_bw() +
  theme_minimal() +
  scale_fill_manual(values = custom_colors) +
  xlab("ChatGPT Release") +
  guides(fill = FALSE) +
  theme(axis.text.y = element_text(margin = margin(r = 45))) +
  theme(axis.text = element_text(size = 16))
        #plot.margin = margin(10, 20, 10, 40))  # Increase left margin (top, right, bottom, left)
dev.off()

shapiro.test(data_before$number_comments)
shapiro.test(data_after$number_comments)

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
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearMilestone", "After"))

pdf("line-chart-questions-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_questions, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Questions Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearMilestone" = "lightpink")) +  # Custom colors
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
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearMilestone", "After"))

pdf("line-chart-answers-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_answers, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Answers Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearMilestone" = "lightpink")) +  # Custom colors
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
                                 ifelse(combined_data$date >= as.Date("2023-11-30") & combined_data$date <= as.Date("2024-04-30"), "OneYearMilestone", "After"))

pdf("line-chart-comments-by-date.pdf")
ggplot(combined_data, aes(x = date, y = number_comments, color = Release)) +
  geom_line(size = 1, na.rm = TRUE) +
  geom_vline(xintercept = as.numeric(as.Date("2022-11-30")), color = "black", linetype = "dashed") +
  geom_vline(xintercept = as.numeric(as.Date("2023-11-30")), color = "black", linetype = "dashed") +  # New vertical line
  labs(title = "Number of Comments Over Time", x = "Date", y = "") +
  scale_color_manual(values = c("Before" = "gray", "After" = "light blue", "OneYearMilestone" = "lightpink")) +  # Custom colors
  theme_minimal() +
  theme(panel.grid = element_blank()) +
  guides(fill = FALSE) +
  theme(axis.text = element_text(size = 14))
dev.off()

