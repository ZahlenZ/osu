library(ggplot2)
# Read in the Iris data set
iris_data <- read.csv("data/irisData.csv")
# Sample mean vector for first 4 columns
iris_mean <- colMeans(iris_data[1:4])
# What is the covariance between Sepal Width and Petal Width
covariance <- cov(iris_data[1:4])
# What is the correlation matrix
correlation <- cor(iris_data[1:4]) 
# Construct all of the pairwise data plots 
# if iris_data$type = (1, 1, 2, 2, 3) then colors = (#0f630c, #0f630c, #108baa, #108baa, #d40bca)
colors <- c("#0f630c", "#108baa", "#d40bca")[unclass(iris_data$Type)]
pairs(iris_data, col = colors)
legend(
    "topright",
    legend = levels(iris_data$Type),
    fill = c("#0f630c", "#108baa", "#d40bca")
)
# Read in cubit data
cubit <- read.csv("data/CubitData.csv")
# Calculate the mean vector
cubit_mean <- colMeans(cubit)
# Calculate the covariance
covariance <- cov(cubit)
# Find the eigen decomposition of the sample covariance matrix
e_cov <- eigen(covariance)
# Make a scatter plot for this data
ggplot(cubit, aes(x = height, y = cubit)) +
    geom_point() +
    geom_segment(
        aes(
            x = cubit_mean[1], 
            y = cubit_mean[2], 
            xend = cubit_mean[1] + 2 * e_cov$vectors[1], 
            yend = cubit_mean[2] + 2 * e_cov$vectors[2]
        ),
        arrow = arrow(length = unit(.5, "cm"))
    )