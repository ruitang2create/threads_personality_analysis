# app.py
import streamlit as st
# from utils.twitter_api import get_user_tweets
# from data.analysis import perform_tweet_analysis

def main():
    st.title("Threads User Personality Analysis")

    # User input for Twitter username
    twitter_username = st.text_input("Enter Threads Username:")

    # if st.button("Analyze Tweets"):
    #     if twitter_username:
    #         st.write(f"Fetching Twitter information for @{twitter_username}...")
    #         user_info = get_user_tweets(twitter_username)

    #         if user_info is not None:
    #             st.write(f"User: {user_info['name']} (@{user_info['screen_name']})")
    #             st.write(f"Followers: {user_info['followers_count']}")
    #             st.write(f"Total Tweets: {user_info['statuses_count']}")
                
    #             st.write("Analyzing tweets...")
    #             analysis_result = perform_tweet_analysis(user_info['tweets'])
    #             st.write("Analysis Result:")
    #             st.write(analysis_result)
    #         else:
    #             st.error("Error: Unable to fetch user information. Please check the Twitter username.")

if __name__ == "__main__":
    main()