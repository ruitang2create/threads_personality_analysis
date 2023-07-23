# Twitter User Information Analysis App

![Twitter User Information Analysis App](app_screenshot.png)

## Overview

This is a simple Streamlit web application that allows users to enter a Twitter username, fetch the user's information, and perform analysis on the user's tweets. The app provides insights into the user's profile, such as the number of followers and total tweets, and displays the results of the tweet analysis.

## Requirements

- Python 3.6 or later
- Streamlit
- Tweepy
- (List any other dependencies your app may have here)

## Setup Instructions

1. Clone this repository to your local machine using the following command:
```
git clone https://github.com/your-github-username/twitter_analysis_app.git
```
2. Navigate to the project directory:
```
cd twitter_analysis_app
```
3. (Optional) Create and activate a virtual environment (recommended) to isolate project dependencies:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install the required dependencies:
```
pip install -r requirements.txt
```

5. Set up your Twitter Developer credentials (API key, API secret key, Access token, and Access token secret) in `utils/twitter_api.py`. This will allow the app to fetch Twitter user information and tweets.

## How to Run

1. After completing the setup instructions, run the Streamlit app using the following command:
```
streamlit run app.py
```

2. The app will start, and you will see a local URL (usually `http://localhost:8501/`) in the terminal.

3. Open your web browser and visit the provided URL to access the app.

## Example Usage

1. Enter a Twitter username in the input field.
2. Click the "Analyze Tweets" button to fetch the user's information and perform the tweet analysis.
3. The app will display the user's profile information, such as the number of followers and total tweets.
4. It will also show the results of the tweet analysis, which can be customized based on your implementation in `data/analysis.py`.

## Additional Notes

- You can customize the tweet analysis logic in `data/analysis.py` to perform different types of analysis on the user's tweets.
- Make sure to respect Twitter's terms of service and API usage policies when using this application.


