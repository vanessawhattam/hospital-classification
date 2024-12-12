# Classification THA


## Assignment
You are now ready to begin assessing your data and build initial models. Randall Cunningham would like you to build decision trees. Your new assignment requires you to build classification trees and regression trees. Use the data file [calihospital.txt](/data/calihospital.txt) for this assignment. 

Decide on the predictor variables you use for these analyses.

### Using `operating income` as a target variable, create a tree (1 pt.)

![operating income regression tree](assets/operInc_tree.png)

Variables included in this tree were: `InOperExp`, `OperRev`, `AvlBeds`, and `NoFTE`.

### Using `operating revenue` as a target variable, create a tree (1 pt.)

![operating revenue tree](assets/operRev_tree.png)

Variables included in this tree were: `OutOperExp`, `OperInc`, `AvlBeds`, and `NetPatRev`.

### Using `TypeControl` as a target variable, create a tree (1 pt.)

![type control classification tree](assets/TypeControl_tree.png)

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| City/County  |    1.00   |  1.00  |   1.00   |    7    |
| District     |    1.00   |  1.00  |   1.00   |   14    |
| Investor     |    1.00   |  1.00  |   1.00   |    3    |
| Non Profit   |    1.00   |  1.00  |   1.00   |   37    |
|--------------|-----------|--------|----------|---------|
| accuracy     |           |        |   1.00   |    61   |
| macro avg    |    1.00   |  1.00  |   1.00   |    61   |
| weighted avg |    1.00   |  1.00  |   1.00   |    61   |


|             | City/County | District | Investor | Non Profit |
|-------------|-------------|----------|----------|------------|
| City/County |      7      |    0     |    0     |      0     |
| District    |      0      |    14    |    0     |      0     |
| Investor    |      0      |    0     |    3     |      0     |
| Non Profit  |      0      |    0     |    0     |     37     |


The variables included in this regression tree were: `NoFTE`, `Teaching`, `AvlBeds`, and `NetPatRev`.

### Using `DonorType` as a target variable, create a tree (1 pt.)

![donor type classification tree](assets/DonorType_tree.png)

|          | precision | recall | f1-score | support |
|----------|-----------|--------|----------|---------|
| Alumni   |    1.00   |  1.00  |   1.00   |    17   |
| Charity  |    1.00   |  1.00  |   1.00   |    44   |
|----------|-----------|--------|----------|---------|
| accuracy |           |        |   1.00   |    61   |
| macro avg|    1.00   |  1.00  |   1.00   |    61   |
| weighted avg |    1.00   |  1.00  |   1.00   |    61   |


|          | Alumni | Charity |
|----------|-------------------|---------------------|
| Alumni |        17         |           0           |
| Charity |        0          |          44          |


The variables included in this tree were: `TypeControl`, `OperInc`, `OperRev`, and `'NetPatRev`. 


## Assess the trees
Interpret your findings for these trees. That is, don't just repeat the English rules found in your splits. Explain why you think the splits you received make sense. (4 pts.)

#### `Operating Income`

The most first splitting variable in this tree was the operating revenue, which is logical given that income and revenue are directly linked to each other, and the revenue can't exceed the income. The tree continued to split primarily on operating revenue for a few levels, however the number of full-time employees makes an appearance around levels four, seven, eight, and ten. Hospitals with larger incomes will have more employees. The number of available beds is a split for levels two and eleven, which does make sense as larger hospitals will have more beds and more money coming in from those beds. Inpatient Operating Expenses makes a guest appearance where larger values will have high operating incomes.

#### `Operating Revenue`

This tree had its initial split on NetPatRev, likely because patient revenues are the largest source of incoming money for hospitals. Net Patient Revenue continues to be an important variable for splitting throughout the tree, as larger patient revenues will result in higher overall operating revenues. Outpatient operating expenses are used for two splits, with larger expenses generally being associated with larger operating revenues because bigger hospitals have more expenses. 

#### `TypeControl`

The type control classification tree first split on Net Patient Revenue, separating larger and smaller City/County-run hospitals. The splits continued to separate out larger and smaller hospitals, splitting on the number of available beds and the number of full-time employees, both of which are positively correlated with hospital size. I didn't specify minimum sample size or minimum nodes, so the tree continued to iterate through each of the continuous variables until each terminal node only had 1-4 observations in the class. Interestingly, the categorical variable `Teaching` was not used in the splits, maybe because hospitals of all control structures can be teaching hospitals so the predictive value was not very high.

#### `DonorType`

This tree was fairly small as there were only two possible outcomes in the class of `DonorType`. Again, the continuous variables appeared to be more important for the splits because `TypeControl` was not used in the splits. The first and third splits were on operating revenue, and these split out the hospitals that had Alumni `DonorType` into those that had small operating revenues from those that had large ones. This was potentially because the `Alumni` class either contributed to small teaching hospitals or large university-type hospitals. Charity hospitals are likely to be mid-sized, as evidenced by their containment within the middle range of splits on the hospital operating revenue. 


## Best Model

Which of these trees would you choose as your best model? Justify your position. (Note, you do not have to use an objective assessment, such as scoring predicted values, due to the small sample size.) (2 pts.)

I think the best model is the `DonorType` tree because it is small and concise, and the terminal nodes are have slightly larger sample sizes than the other trees. Additionally, this tree was 100% in the confusion matrix showing a high level of accuracy for a relatively small amount of computing power needed to generate the splits. Admittedly, this tree has fewer possible outcomes because there are only 2 levels of `DonorType`, so the splits can be more easily determined. 