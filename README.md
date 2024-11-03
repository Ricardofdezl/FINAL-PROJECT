# FINAL-PROJECT

 · Overview:
- Download 5 datasets from Kaggle(Footlocker, ASOS, H&M, Mango and Zara). -
- Webscrapping "Massimo Dutti" website and downloaded the relevant data for both men and women. 
- Import all the necessary libraries.
- Create a dataframe for each dataset.
- Clean and organize each dataset separately.
- Calculate the mean price for each dataset.
- Create csv for each dataset after being cleaned (for later usage in Tableau).
- Concatenate the 6 datasets (brands_df) and drop the necessary columns.
- Combine data from various columns into new consolidated columns, then clean up redundant columns to refine the Dataframe.
- Rename brands_df as df_cleaned and drop innecesary columns.
- Manage all the null values in different ways (dropping columns, filling with mode, filling with strings).
- Create a csv for df_cleaned.
  
  · EDA:
- Compute mean price for each group per section and display it in a bar chart.
- Compute average price for each brand and display it in a bar chart.
- Display in a barchart and dataframe for Footlocker's top 10 brands.
- Create a pie chart representing the relationship between sales volume and promotion in Zara.
- Display in a barchart H&M's top 10 colors.
- Display in a barchart ASOS top 10 colors.
- Display in a barchart and dataframe for Mango's top 10 categories by product.
- Display in a barchart and dataframe for Massimo Duti's top 10 categories by average price.
- Create a histogram for the price of the whole dataset (df_cleaned). 

  · HYPOTHESIS TESTING:
- Compute One Sample T-Test, with its corresponding hypotheses, significance level and its values well defined and calculated in order to compare it with alpha and reject or accept H0. 
- Compute two more tests but this time Two Sample T-Test with independent variables.
- The last test was a Proportion Z-Test with both hypotheses and values well defined in order to compare it and reject H0.
  
  · MACHINE LEARNING: (Different notebook) 
 - Import the necessary libraries.
 - Import and defined as "brands" brands_csv.
 - Create a Correlation Matrix dropping all the columns and just taking into account 'price', 'promotion' and 'section' .
 - Apply feature scaling to numerical columns (price).
 - Train-test split process, defining the feature and target.
 - Linear regression model and its corresponding evaluation (R², MAE and RMSE).
 - Decision Tree model and its corresponding evaluation (R², MAE and RMSE).
 - Random Forest model and its corresponding evaluation (R², MAE and RMSE).
 - Gradient Boosting and its corresponding evaluation (R², MAE and RMSE).
 - Hyperparameter Tuning for Random Forest to look for the best params and score.
 - Hyperparameter Tuning for Gradient Boosting to look for the best params and score.
 - Compare the two hyperparameters tunning and create a csv with the best model (Gradient Boosting).
 - Display the results of the actual price and it's prediction.

   · SQL:
- Import both "brands.csv" and "gradient_boosting_predictions.csv" into SQL workbench.
- Create a database for each csv.
- Confirm that each csv was well imported and display their corresponding columns and values.
- Save both SQL files.

   · TABLEAU:
- Import the 6 cleaned csv into different Data Sources.
- Analyze each database in two different ways. (we have changed from dimension to measure some of the fields when needed).
- Create a dashboard for each database showing both sheets with their corresponding filters. 
