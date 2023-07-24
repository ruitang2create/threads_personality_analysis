# app.py
import streamlit as st
# from utils.twitter_api import get_user_tweets
# from data.analysis import perform_tweet_analysis
from data.parse_threads import fetch_user_threads, fetch_user_info

def main():
    st.title("Threads User Personality Analysis")

    # User input for Twitter username
    threads_username = st.text_input("Enter Threads Username:")

    if st.button("Analyze Threads"):
        if threads_username:
            st.write(f"Fetching threads for @{threads_username}...")
            user_info = fetch_user_info(threads_username)
            # st.json(user_info)

            if user_info is not None:
                user_obj = user_info.get("data").get("userData").get("user")
                full_name = user_obj.get("full_name")
                follower_count = user_obj.get("follower_count")
                st.write(f"User: {threads_username} (@{full_name})")
                st.write(f"Followers: {follower_count}")
                # st.write(f"Total Tweets: {user_info['statuses_count']}")
                
                st.write("Analyzing threads...")
                user_threads = fetch_user_threads(threads_username)
                threads_meta = user_threads.get("data").get("mediaData").get("threads")
                st.json(user_threads)
                # analysis_result = perform_tweet_analysis(user_info['tweets'])
                st.write("Analysis Result:")
                # st.write(analysis_result)
            else:
                st.error("Error: Unable to fetch user information. Please check the Threads username.")

if __name__ == "__main__":
    main()