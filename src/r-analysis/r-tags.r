library(rstatix)
#files <- list("/home/leuson/Downloads/teste/output-library/before/", "/home/leuson/Downloads/teste/output-library/after/")
files <- list("/home/leusonmario/postdoctoral/projects/chat-stack/data/before/library/", "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/library/")
tags <- list("pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter")
pls <- list("python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c")
frameworks <- list("reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel", "vue.js")

for (x in 1:10){
    print(paste("Analysis for Tag: ",tags[x], sep=""))

    file_path_before <- paste(files[1],tags[x],"-tag.csv", sep="")
    file_path_after <- paste(files[2],tags[x],"-tag.csv", sep="")

    data_before <- read.csv(file_path_before)
    data_after <- read.csv(file_path_after)

    shapiro_test_before <- shapiro.test(data_before$value)
    shapiro_test_after <- shapiro.test(data_after$value)

    print(shapiro_test_before)
    print(shapiro_test_after)

    column_name <- "value"  # Change this if needed
    if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
      stop("Column 'value' not found in one of the CSV files!")
    }

    # Combine datasets for independent (unpaired) test
    data <- data.frame(
      value = c(data_before[[column_name]], data_after[[column_name]]),
      group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
    )

    # Perform Wilcoxon test
    wilcox_result <- wilcox_test(data, value ~ group)

    # Compute effect size
    effect_size <- wilcox_effsize(data, value ~ group)

    # Print results
    print(wilcox_result)
    print(effect_size)

}

files <- list("/home/leusonmario/postdoctoral/projects/chat-stack/data/before/pl/", "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/pl/")
tags <- list("pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter")
pls <- list("python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c")
frameworks <- list("reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel", "vue.js")

for (x in 1:10){
    print(paste("Analysis for Programming Languages: ",pls[x], sep=""))

    file_path_before <- paste(files[1],pls[x],"-tag.csv", sep="")
    file_path_after <- paste(files[2],pls[x],"-tag.csv", sep="")

    data_before <- read.csv(file_path_before)
    data_after <- read.csv(file_path_after)

    shapiro_test_before <- shapiro.test(data_before$value)
    shapiro_test_after <- shapiro.test(data_after$value)

    print(shapiro_test_before)
    print(shapiro_test_after)

    column_name <- "value"  # Change this if needed
    if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
      stop("Column 'value' not found in one of the CSV files!")
    }

    # Combine datasets for independent (unpaired) test
    data <- data.frame(
      value = c(data_before[[column_name]], data_after[[column_name]]),
      group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
    )

    # Perform Wilcoxon test
    wilcox_result <- wilcox_test(data, value ~ group)

    # Compute effect size
    effect_size <- wilcox_effsize(data, value ~ group)

    # Print results
    print(wilcox_result)
    print(effect_size)

}

files <- list("/home/leusonmario/postdoctoral/projects/chat-stack/data/before/framework/", "/home/leusonmario/postdoctoral/projects/chat-stack/data/after/framework/")
tags <- list("pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter")
pls <- list("python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c")
frameworks <- list("reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel", "vue.js")

for (x in 1:10){
    print(paste("Analysis for Frameworks: ",frameworks[x], sep=""))

    file_path_before <- paste(files[1],frameworks[x],"-tag.csv", sep="")
    file_path_after <- paste(files[2],frameworks[x],"-tag.csv", sep="")

    data_before <- read.csv(file_path_before)
    data_after <- read.csv(file_path_after)

    shapiro_test_before <- shapiro.test(data_before$value)
    shapiro_test_after <- shapiro.test(data_after$value)

    print(shapiro_test_before)
    print(shapiro_test_after)

    column_name <- "value"  # Change this if needed
    if (!(column_name %in% colnames(data_before) & column_name %in% colnames(data_after))) {
      stop("Column 'value' not found in one of the CSV files!")
    }

    # Combine datasets for independent (unpaired) test
    data <- data.frame(
      value = c(data_before[[column_name]], data_after[[column_name]]),
      group = rep(c("before", "after"), c(nrow(data_before), nrow(data_after)))
    )

    # Perform Wilcoxon test
    wilcox_result <- wilcox_test(data, value ~ group)

    # Compute effect size
    effect_size <- wilcox_effsize(data, value ~ group)

    # Print results
    print(wilcox_result)
    print(effect_size)

}