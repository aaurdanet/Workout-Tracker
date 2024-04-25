# Workout-Tracker

This program is designed to help you track your workouts and upload the data to a spreadsheet for easy management and analysis.
Setup

    Environment Variables:
    Ensure you have the following environment variables set:
    APP_ID: Your application ID for workout API.
    WORKOUT_API_KEY: Your API key for workout API.
    SHEET_TOKEN: Authorization token for accessing the spreadsheet API.
    WEIGHT: Your weight in kilograms.
    HEIGHT: Your height in centimeters.
    AGE: Your age.
    nutritionix_endpoint: Endpoint for the Nutritionix API https://www.nutritionix.com/business/api
    sheet_endpoint: Endpoint for the Sheety API https://sheety.co/

Dependencies:
Make sure you have the necessary dependencies installed. You can install them via pip:

    pip install requests

Usage

Run the Program:
Run the program using a Python interpreter.
You will be prompted to input your workout details.

Input:
Enter your workout details as prompted, including the type of workout.

Output:
The program will fetch workout data and upload it to your designated spreadsheet.

Data:
The data uploaded includes the date, time, exercise, duration, and calories burnt.

Confirmation:
Upon successful upload, the program will display a confirmation message.

Notes

Make sure you have a stable internet connection to fetch data and upload it to the spreadsheet.
Ensure your environment variables are correctly set to access the required APIs.
Review the code comments for more detailed information on each step.
