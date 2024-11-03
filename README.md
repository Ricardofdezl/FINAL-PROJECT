# FINAL-PROJECT

Overview:
- In this project we got 5 datasets from Kaggle(Footlocker, ASOS, H&M, Mango and Zara) and 1 doing webscraping (Massimo Duti).
- Import all the necessary libraries.
- Create a dataframe for each dataset.
- Clean and organize each dataset separately.
- Calculate the mean price for each dataset.
- Create csv's for each dataset after being cleaned (for later usage in Tableau).
- Concatenate the 6 datasets (brands_df) and drop the necessary columns.
- Combine data from various columns into new consolidated columns, then clean up redundant columns to refine the Dataframe.
- Rename brands_df as df_cleaned and drop innecesary columns.
- Manage all the null values in different ways (dropping columns, filling with mode, filling with strings).
- Create a csv for df_cleaned.
  -EDA:
   - Compute mean price for each group per section and display it in a bar chart.
   - Compute average price for each brand and display it in a bar chart.
   - Display in a barchart Footlocker's top 10 brands.
   - Create a pie chart representing the relationship between sales volume and promotion in Zara.
   - Display in a barchart H&M's top 10 colors.
   - Display in a barchart ASOS top 10 colors.
   - Display in a barchart Mango's top 10 categories by product.
   - Display in a barchart Massimo Duti's top 10 categories by average price.

-HYPOTHESIS TESTING:
   - One sample T-Test: H0: avg prices for Man == 55
                        H1: avg prices for Man != 55
  
   -Two Sample T-Test(Indep): H0: mu price male >= mu price female
                              H1: mu price male < mu price female
   
   -Two Sample T-Test(Indep): H0: mu price Zara >= mu price Massimo Duti
                              H1: mu price Zara < mu price Massimo Duti
   
   -Proportion Z-Test: H0: proportion of 'shoes' in the dataset = 0.3 
                       H1: proportion of 'shoes' in the dataset!= 0.3



-MACHINE LEARNING: GD Predictive Model (price prediction)
 
 -In another notebook, import the necessary libraries.
 
 -import brands_csv.
 
 -Create a Correlation Matrix just taking into account 'price', 'promotion'and 'section'.
 
 -Apply feature scaling to numerical columns.
 
 -Do a Train-test split process.
 
 -Do a linear regression model and its evaluation.
 
 -Do Decision Tree model.
 
 -Do Random Forest model.
 
 -Do Gradient Boosting.
 
 -Do hyperparameter Tuning for Random Forest.
 
 -Do hyperparameter Tuning for Gradient Boosting.
 
 -Create a csv with the best model.
 
 -Display the results of the actual price and it's prediction.
