# sp_analytics

Final Capstone project for Data Science Capstone and Ethics class.

Analytics & visualization platform for a telecommunications company.

Setting up SP_Analytics project

PostgreSQL as the backend. Database Name: sp_analytics


Copying data from previous temporary dtabase

	- pg_dump -t events -t cells -t amenities postgres | psql sp_analytics 

Creating a new application user then granting full access on all tables

	- CREATE create user capstone with password 'sp';
	- GRANT ALL PRIVILEGES ON events TO capstone;
	- GRANT ALL PRIVILEGES ON cells TO capstone;
	- GRANT ALL PRIVILEGES ON amenities TO capstone;

### Project Details (Tech Stack + Analytics Methods)

Using Flask Python Framework for reporting and analytics

Using PsycoPG2 for data access from within Flask

#########################################

Steps in modeling:

1. Collect relevant data from the source 
    - If data is too big, then take sufficient stratified sample of the data to perform the upcoming steps in modeling
2. Identify the problem/opportunity to be solved or analyzed
    - Perform Exploratory Data Analysis on the data using using summary statistics, plots, etc to have a clear understanding of the problem and the potential solutions
3. Perform outlier detection using
    - density/histogram/scatter plots of each variable
    - summary statistics
    - median/interquantile absolute deviation method
4. Data Preprocessing and Feature Engineering
    - Imputing missing and invalid data
    - Properly transforming variables to the proper type 
    - Normalization, one-hot encoding, etc
5. Feature Selection and Model Evaluation
    - Randomly split the data/sample into test and train datasets
    - Use k-fold cross validation on the train data to:
        - Select the combination of features to use in the model
        - Select the best learning algorithm to use (e.g. Random Forest, SVM, etc)
        - perform hyperparameter tuning for the selected model
6. Train the model using the full train dataset
7. Evaluate your model using the full test dataset and explore the results to identify errors, misclassifications, etc to improve the model and repeat the above steps
8. Once satisfied with the performance of the model on the sample data then automate the steps.
Contact GitHub API Training Shop Blog About
