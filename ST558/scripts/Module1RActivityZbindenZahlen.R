library(ggplot2)
library(GGally)
# read csv from local directory
data <- read.csv("ST558/data/SeedsData.csv")
# Question 1: data dimentions
data_dimension <- dim(data)
# Question 2a: first 6 rows (head)
data_head <- head(data)
# Question 2b: last 6 rows (tail)
data_tail <- tail(data)
# Question 3: default summary statistics
summary_statistics <- summary(data)
# Question 4: data types
data_types <- str(data)
data_types_alt <- sapply(data, class)
# Question 5: appropriate data types
data$Variety <- as.factor(data$Variety)
# Question 6: produce histograms 
# plot for area
ggplot(data, aes(x = Area)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for perimeter
ggplot(data, aes(x = Perimeter)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for compactness
ggplot(data, aes(x = Compactness)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for length
ggplot(data, aes(x = Length)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for width
ggplot(data, aes(x = Width)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for asymmetry
ggplot(data, aes(x = Asymmetry)) + 
    geom_histogram(fill = "blue", color = "black")
# plot for groovelength
ggplot(data, aes(x = GrooveLength)) + 
    geom_histogram(fill = "blue", color = "black")
# Question 7: pairwise scatter plot
ggpairs(data, title = "Pairwise Scatterplot")
# Question 8: mean vector
mean_vector <- colMeans(data[1:7])
# Question 9: covariance matrix
covariance_matrix <- cov(data[1:7])
# Question 10: correlation matrix
correlation_matrix <- cor(data[1:7])
# Create modified dataset
data_mod <- data
data_mod$Compactness <- data_mod$Compactness * 100
# Question 11: sample mean vector for modified data
mean_vector_mod <- colMeans(data[1:7])
# Question 12: sample covariance matrix for modified data
cov_mod <- cov(data[1:7])
# Question 13: sample correlation matrix for modified data
cor_mod <- cor(data[1:7])
# Create a modified dataset
seeds_mod2 <- data
seeds_mod2$Asymmetry <- seeds_mod2$Asymmetry - mean(seeds_mod2$Asymmetry)
# Question 15: sample mean vector of modified dataset
mean_vec_mod2 <- colMeans(seeds_mod2[1:7])
summary_mod2 <- summary(seeds_mod2)
# Question 16: sample covariance matrix
cov_mat_mod <- cov(seeds_mod2[1:7])
# Question 17: sample correlation matrix
cor_mat_mod <- cor(seeds_mod2[1:7])