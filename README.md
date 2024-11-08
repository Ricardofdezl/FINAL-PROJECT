# FINAL-PROJECT

 · Overview:
- Downloaded 5 datasets from Kaggle(Footlocker, ASOS, H&M, Mango and Zara). -
- Webscrapped "Massimo Dutti" website and downloaded the relevant data for both men and women. 
- Imported all the necessary libraries.
- Created a dataframe for each dataset.
- Cleaned and organize each dataset separately.
- Calculated the mean price for each dataset.
- Created csv for each dataset after being cleaned (for later usage in Tableau).
- Concatenated the 6 datasets (brands_df) and drop the necessary columns.
- Combined data from various columns into new consolidated columns, then clean up redundant columns to refine the Dataframe.
- Renamed brands_df as df_cleaned and drop innecesary columns.
- Managed all the null values in different ways (dropping columns, filling with mode, filling with strings).
- Created a csv for df_cleaned.
  
  · EDA:
- Computed mean price for each group per section and display it in a bar chart.
- Computed average price for each brand and display it in a bar chart.
- Displayed in a barchart and dataframe for Footlocker's top 10 brands.
- Created a pie chart representing the relationship between sales volume and promotion in Zara.
- Displayed in a barchart H&M's top 10 colors.
- Displayed in a barchart ASOS top 10 colors.
- Displayed in a barchart and dataframe for Mango's top 10 categories by product.
- Displayed in a barchart and dataframe for Massimo Duti's top 10 categories by average price.
- Created a histogram for the price of the whole dataset (df_cleaned). 

  · HYPOTHESIS TESTING:
- Computed One Sample T-Test, with its corresponding hypotheses, significance level and its values well defined and calculated in order to compare it with alpha and reject or accept H0. 
- Computed two more tests but this time Two Sample T-Test with independent variables.
- The last test was a Proportion Z-Test with both hypotheses and values well defined in order to compare it and reject H0.
  
  · MACHINE LEARNING: (Different notebook) 
 - Imported the necessary libraries.
 - Imported and defined as "brands" brands_csv.
 - Created a Correlation Matrix dropping all the columns and just taking into account 'price', 'promotion' and 'section' .
 - Applyed feature scaling to numerical columns (price).
 - Train-test split process, defining the feature and target.
 - Linear regression model and its corresponding evaluation (R², MAE and RMSE).
 - Decision Tree model and its corresponding evaluation (R², MAE and RMSE).
 - Random Forest model and its corresponding evaluation (R², MAE and RMSE).
 - Gradient Boosting and its corresponding evaluation (R², MAE and RMSE).
 - Hyperparameter Tuning for Random Forest to look for the best params and score.
 - Hyperparameter Tuning for Gradient Boosting to look for the best params and score.
 - Compared the two hyperparameters tunning and create a csv with the best model (Gradient Boosting).
 - Displayed the results of the actual price and it's prediction.

   · SQL:
- Imported both "brands.csv" and "gradient_boosting_predictions.csv" into SQL workbench.
- Created a database for each csv.
- Confirmed that each csv was well imported and display their corresponding columns and values.
- Saved both SQL files.

   · TABLEAU:
- Imported the 6 cleaned csv into different Data Sources.
- Analyzed each database in two different ways. (we have changed from dimension to measure some of the fields when needed).
- Created a dashboard for each database showing both sheets with their corresponding filters. 

  · APP CREATION:
- Created a copy of the "brands_final_project.ipynb" file and converted it into a Python script for improved modularity and usability.
- Defined a "load_data()" function within this Python file to handle loading the entire "brands.csv" dataset.
- Developed an additional Python file dedicated to app creation using Streamlit.
- Imported Streamlit to build an interactive user interface.
- Imported the data-handling script to utilize the "load_data()" function.
- Implemented filter options to enable users to filter brands by key attributes: Brand, Section, Price Range, and Category.
- Executed the Streamlit script in the terminal, generating a link to our fully functional app, complete with filtering capabilities for user exploration of the dataset.
This README section provides a clear summary of the project structure, functionality, and app deployment steps.
