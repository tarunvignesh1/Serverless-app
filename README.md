Here is a `README.md` file for your GitHub repository:

---

# Workout Tracker using AWS Serverless services (Lambda, API gateway, DynamoDB and Amplify)

## Overview

The Workout Tracker is a web application that allows users to log their workout details and visualize their workout hours over a week. This project utilizes AWS services (API Gateway, Lambda, and DynamoDB) for the backend and a simple HTML/CSS/JavaScript frontend.

## Project Structure

### Frontend

- **`index.html`**: Contains the form for inputting workout data and the chart for displaying workout hours.
- **`styles.css`**: Provides the styling for the HTML form and chart, including a dark theme design.
- **`script.js`**: JavaScript file for handling form submissions, making API calls, and rendering the workout chart.

### Backend

- **`lambda_post_function.py`**: AWS Lambda function to handle POST requests for saving workout data to DynamoDB.
- **`lambda_get_function.py`**: AWS Lambda function to handle GET requests for retrieving workout data from DynamoDB.

### AWS Configuration

- **DynamoDB Table**: 
  - **Table Name**: `WorkoutData`
  - **Primary Key**: `username` (String)
  - **Attributes**: `workoutDay` (String), `hours` (Number), `workoutDate` (String)

- **API Gateway**:
  - **POST Endpoint**: Connects to the Lambda function that saves workout data.
  - **GET Endpoint**: Connects to the Lambda function that retrieves workout data.

## Setup Instructions

### 1. DynamoDB Configuration

1. Create a DynamoDB table named `WorkoutData` with the following attributes:
   - **Primary Key**: `username` (String)
   - **Attributes**: `workoutDay` (String), `hours` (Number), `workoutDate` (String)

### 2. AWS Lambda Functions

1. Create two Lambda functions:
   - **`lambda_post_function.py`**: For handling POST requests and saving data to DynamoDB.
   - **`lambda_get_function.py`**: For handling GET requests and retrieving data from DynamoDB.

2. Ensure these Lambda functions are properly connected to API Gateway endpoints.

### 3. API Gateway Setup

1. Create an API with the following endpoints:
   - **POST Endpoint**: `/post` to integrate with the Lambda function for saving data.
   - **GET Endpoint**: `/get` to integrate with the Lambda function for retrieving data.

2. Configure the methods and ensure they accept `application/json`.

### 4. Frontend Setup

1. Deploy the `index.html`, `styles.css`, and `script.js` files to a web server or hosting service of your choice.

2. Update the API endpoint URLs in `script.js` to match your deployed API Gateway endpoints.

## Usage

1. **Submit Workout Data**: Fill out the form in `index.html` and submit to log workout details.
2. **View Workout Data**: The chart will automatically update to display the logged workout data.



Feel free to adjust any section or add more details as needed for your specific setup and use case.
