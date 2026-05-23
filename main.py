from src.pharma_adherence.data import PharmaDataset
from src.pharma_adherence.modeling import ModelTrainer

"""
DAY 1: DATA PREPROCESSING & ANALYSIS
"""

dataset = PharmaDataset("data/raw/prescriptions_large_raw.csv")
print(dataset.df.head())

#TODO: Clean the dataset
dataset.clean()

#TODO: Save the dataset as a csv into "data/processed/"
dataset.save("data/processed/prescriptions_large_cleaned.csv")

#TODO: Visualize the cleaned data

#TODO: Look at the summary of a patient

"""
DAY 2: MACHINE LEARNING
"""

#TODO: Instantiate a linear regression trainer
linear_model = ModelTrainer(dataset.df, "proportion_days_covered", ["sex", "copay_amount"])

#TODO: Train the linear model
model, metrics = linear_model.train_linear()

#TODO: Print the linear model metrics
print(metrics)

#TODO: Instantiate a logistic regression trainer

#TODO: Train the logistic model

#TODO: Print the logistic model metrics