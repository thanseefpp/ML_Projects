# Polynomial Regression

#Importing Dataset

dataset = read.csv('Data.csv')

# Taking the values of the dataset contains actual values and replacing to the variable.
# dataset = dataset[2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Polynomial Regression to the dataset
# Create you regressor here.

# Predicting a new result with Polynomial Regression
y_pred_using_poly = predict(regressor,data.frame(Level = 6.5))

library(ggplot2)

# Visualizing the Regression Model result (For Higher resolution and smoother curve)

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
  
ggplot() +
  geom_point(aes(x= dataset$Level, y= dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor,newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (Regression Model)') +
  xlab('Level') +
  ylab('Salary')


