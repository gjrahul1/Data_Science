#### Cross Validation
Cross-validation is a statistical method used to estimate the skill of machine learning models.

It is commonly used in applied machine learning to compare and select a model for a given predictive modeling problem because it is easy to understand, easy to implement, and results in skill estimates that generally have a lower bias than other methods.

#### k-Fold Cross-Validation
Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample.

The procedure has a single parameter called k that refers to the number of groups that a given data sample is to be split into.

As such, the procedure is often called k-fold cross-validation.

It is a popular method because it is simple to understand and because it generally results in a less biased or less optimistic estimate of the model skill than other methods, such as a simple train/test split.

| Step | Description                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| 1    | Shuffle the dataset randomly.                                                                |
| 2    | Split the dataset into k groups.                                                             |
| 3.1  | Take one group as a hold-out or test dataset.                                                |
| 3.2  | Take the remaining groups as a training dataset.                                             |
| 3.3  | Fit a model on the training set and evaluate it on the test set.                             |
| 3.4  | Retain the evaluation score and discard the model.                                           |
| 4    | Summarize the skill of the model using the sample of model evaluation scores.                |


- A value of k=10 is very common in the ﬁeld of applied machine learning, and is recommend
if you are struggling to choose a value for your dataset.


> This approach involves randomly dividing the set of observations into k groups, or folds, of approximately equal size.  
>  
> The ﬁrst fold is treated as a validation set, and the method is ﬁt on the remaining k − 1 folds.  
>  
> — *Page 181, An Introduction to Statistical Learning, 2013*
> To summarize, there is a bias-variance trade-oﬀ associated with the choice of k in k-fold cross-validation.
> 
> Typically, given these considerations, one performs k-fold cross-validation using k = 5 or k = 10, as these values have been shown empirically to yield test error rate estimates that suﬀer neither from excessively high bias nor from very high variance.
>
>  — *Page 184, An Introduction to Statistical Learning, 2013*
