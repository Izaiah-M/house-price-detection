# Bengaluru House Price Prediction Model

This project is a simple price prediction model designed to predict the price of houses based on several key features such as location, BHK, baths, and square footage (sqft). The model uses the **Bengaluru House Price dataset** and serves as an introductory project to data cleaning, exploratory data analysis (EDA), feature generation for machine learning, and building a **Linear Regression model**.

## Table of Contents

- [Dataset](#dataset)
- [Features](#features)
- [Model](#model)
- [UI](#ui)
- [API](#api)
- [Setup](#setup)
- [Deployment](#deployment)
- [License](#license)

## Dataset

The dataset used in this project is the [Bengaluru House Price dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data?resource=download) available on Kaggle. The dataset contains house prices in Bangalore, along with details like location, size, BHK, baths, and area (sqft).

## Features

- **Location:** The geographical area where the house is located.
- **BHK:** Number of bedrooms, halls, and kitchens in the house.
- **Baths:** The number of bathrooms.
- **Sqft:** Total area of the house in square feet.

## Model

The model uses a **Linear Regression** approach to predict house prices. Steps involved include:

- **Data Cleaning:** Handling missing values, removing outliers, and converting categorical features.
- **EDA:** Exploratory data analysis to understand feature relationships.
- **Feature Generation:** Creating and selecting key features for the model.
- **Training:** The model is trained on the dataset and tested for accuracy.

## UI

The project features a simple user interface built using **React**, deployed on **Vercel**. Users can input the necessary details (location, BHK, baths, and sqft) to get a price prediction.

**UI Link:** [Insert Vercel Link Here]

## API

The prediction API is built using **Flask** and is deployed on **Render**. The API accepts house details and returns a predicted price.

**API Link:** [Insert Render Link Here]

## Setup

### Requirements

- Python 3.7+
- Flask
- Scikit-learn
- Pandas
- React
- Node.js
