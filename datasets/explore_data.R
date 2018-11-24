
###### training_data ###### 
data <- read.csv("training_data/training_data.csv")
#
head(data)
#
ncol(data) # nr features
nrow(data) # nr observations
colnames(data) 

# data type insight
str(data)
table(sapply(data, is.numeric))
table(sapply(data, is.integer))
table(sapply(data, is.factor))
table(sapply(data, is.character))
table(sapply(data, is.double))

# total nr columns
colnames(data)

# nr missing values column-wise on different rates
sum(colSums(is.na(data)) / nrow(data) > 0.99)
sum(colSums(is.na(data)) / nrow(data) > 0.95)
sum(colSums(is.na(data)) / nrow(data) > 0.9)
sum(colSums(is.na(data)) / nrow(data) > 0.5)



###### training_data_attacks.csv ###### 

data_attacks <- read.csv("training_data/training_data_attacks.csv")
head(data_attacks)
#
ncol(data_attacks) # nr features
nrow(data_attacks) # nr observations
colnames(data_attacks) 

# compare columns
library(compare)

#
# nr missing values column-wise on different rates
sum(colSums(is.na(data_attacks)) / nrow(data_attacks) > 0.99)



###### challenging_no2.csv --> smaller dataset #####

data_ch2 <- read.csv("challenging_data/challenging_no2.csv")

head(data_ch2)
str(data_ch2)

ncol(data_ch2) # nr features
nrow(data_ch2) # nr observations
colnames(data_ch2) 


# nr missing values column-wise on different rates
sum(colSums(is.na(data_ch2)) / nrow(data_ch2) > 0.99)

# sparsity of the dataset
sum(data_ch2==0) / prod(dim(data_ch2))

# sparsity of the dataset
sum(data_ch2==0) / prod(dim(data_ch2))


###### challenging_no1.csv --> smaller dataset #####

data_ch1 <- read.csv("challenging_data/challenging_no1.csv")

head(data_ch1)
str(data_ch1)

ncol(data_ch1) # nr features
nrow(data_ch1) # nr observations
colnames(data_ch1) 


# nr missing values column-wise on different rates
sum(colSums(is.na(data_ch1)) / nrow(data_ch1) > 0.99)

# sparsity of the dataset
sum(data_ch1==0) / prod(dim(data_ch1))

