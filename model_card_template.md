# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This project uses a Random Forest Clssifier from the scikit-learn library to predict if an individual's
annual income exceeds $50k based on demographic and employment data from the Census dataset.

## Intended Use
This model intends to predict if an individual's annual income is greater than 50k using demographic
and employment information. It's designed for an educational project and should not be used for decision
making outside of this project.

## Training Data
The model was trained using the Census dataset provided. The dataset contains demographic and employment
data such as age, education, marital status, race, sex, and occupation among other characteristics. These
characteristics were used to predict if an individual's annual income exceeds $50k.

## Evaluation Data
The model was evaluated using a test set created with a 20/80 train/test split. The test data test data
wasn't used during training and was used to measure the model's performance.

## Metrics
The model was evaluated using precision, recall, and F1 score. On the test dataset, it achieved a
precision score of 0.7410, a recall of 0.6321, and an F1 score of 0.6822. These metrics indicate the
model is correctly classifying if an individual's annual income exceeds $50,000.

## Ethical Considerations
The Census income dataset contains demographic information such as age, race, sex, and native country. As
a result, the model may learn or reinforce biases. Predictions from the model shouldn't be used as 
the sole basis for making decisions that can greatly affect individuals, such as financial or employment
decisions.

## Caveats and Recommendations
This model was created for educational purposes using the Census dataset provided and may not generalize to
other datasets or real world populations. If the model were to be used in practice, it should be evaluated
on more diverse and updated data. It should be monitored and retrained as needed to preserve fairness and 
improve performance.