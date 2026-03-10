# ds4420_final_project

In this project, we will model the Energy Information Administration's public natural gas storage level data. Natural gas storage levels significantly impact natural gas prices and the plethora of  financial derivatives tracking them, therefore, building an accurate and explainable model predicting natural gas storage is an important problem with many direct applications. 

# Method

The SARIMA model is conducive to model natrual gas storage levels because it is specifically designed to handle a strong seasonal component. Storage levels drop in the winter months as natural gas powered heating demand rises, forming a strong seasonal pattern with a yearly frequency.

# Preliminary Conclusion 

After hyperparameter tuning, a SARIMA model with parameters (26, 0, 5) and Seasonal order (2, 1, 2, 52) is the most accurate. On the test set of 2025 and 2026 data, it achieved an rmse of 131.21

