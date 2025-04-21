files <- list("/home/leusonmario/postdoctoral/projects/chat-stack/data/after/library/", "/home/leusonmario/postdoctoral/projects/chat-stack/datayear2/year/")
tags <- list("pandas", "dataframe", "arrays", "json", "jquery", "numpy", "string", "pyspark", "ggplot2", "tkinter")
pl <- list("python", "javascript", "java", "c#", "r", "php", "typescript", "c++", "dart", "c")
framework <- list("reactjs", "android", "node.js", "flutter", "django", "angular", "react-native", "spring-boot", "laravel", "vue.js")

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

    wilcox_test <- wilcox.test(data_before$value, data_after$value)

    # Print the test results
    print(wilcox_test)
}
