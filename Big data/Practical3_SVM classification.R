#Code for installation of all necessary packages
install.packages("caret")
install.packages("ggplot2")
install.packages("GGally")
install.packages("psych")
install.packages("ggpubr")
install.packages("reshape")
# Code for importation of all necessary packages
library(caret)
library(ggplot2)
library(GGally)
library(psych)
library(ggpubr)
library(reshape)
# Code
df <- read.csv("C:/Users/DELL/Downloads/diabetes.csv")
head(df)

# Code
sum(is.na(df))
# Code
dim(df)

# Code
sapply(df, class)
# Code
summary(df) # to calculate the summary of our dataset

# Code
a <- ggplot(data = df, aes(x = Pregnancies)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
b <- ggplot(data = df, aes(x = Glucose)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
c <- ggplot(data = df, aes(x = BloodPressure)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
d <- ggplot(data = df, aes(x = SkinThickness)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
e <- ggplot(data = df, aes(x = Insulin)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
f <- ggplot(data = df, aes(x = BMI)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
g <- ggplot(data = df, aes(x = DiabetesPedigreeFunction)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +
  geom_density()
h <- ggplot(data = df, aes(x = Age)) +
  geom_histogram( color = "red", fill = "blue", alpha = 0.1) +geom_density()
ggarrange(a, b, c, d,e,f,g, h + rremove("x.text"),
          labels = c("a", "b", "c", "d","e", "f", "g", "h"),
          ncol = 3, nrow = 3)

# Code
ggplot(data = df, aes(x =Outcome, fill = Outcome)) +
  geom_bar()

# Code to label our categorical variable as a factor
df$Outcome<- factor(df$Outcome,
                    levels = c(0, 1),
                    labels = c("Negative", "Positive"))
out <- subset(df,
              select = c(Pregnancies,Glucose,
                         BloodPressure,SkinThickness,
                         Insulin,BMI,
                         DiabetesPedigreeFunction,Age))
# Code for boxplot
ggplot(data = melt(out),
       aes(x=variable, y=value)) +
  geom_boxplot(aes(fill=variable))

corPlot(df[, 1:8])

cutoff <- createDataPartition(df$Outcome, p=0.85, list=FALSE)
# select 15% of the data for validation
testdf <- df[-cutoff,]
# use the remaining 85% of data to training and testing the models
traindf <- df[cutoff,]
# Code to train the SVM
set.seed(1234)
# set the 10 fold cross validation with AU
# to pick for us what we call the best model
control <- trainControl(method="cv",number=10, classProbs = TRUE)
metric <- "Accuracy"
model <- train(Outcome ~., data = traindf, method = "svmRadial",
               tuneLength = 8,preProc = c("center","scale"),
               metric=metric, trControl=control)
# Code for model summary
model

# Code
plot(model)
