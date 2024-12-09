import streamlit as st
from helper import get_summary, fetch_news, fetch_news_links
from helper import evaluate_tokenizer_quality, nlp
# Set up the configuration for the Streamlit web app

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': 'This is a Text Summarization Web App. It summarizes news articles or custom input text!'
    }
)

# Sidebar configuration
st.sidebar.title("Text Summarization Web App")
option = ["News Summary and Headlines", "Custom Text Summarization"]
choice = st.sidebar.selectbox("Select your choice", options=option)

# Custom Text Summarization option
if choice == "Custom Text Summarization":
    st.sidebar.markdown("Copy and paste your text in the text area below to get a summary.")
    st.title("Welcome to Custom Text Summarization")
    col1, col2 = st.columns(2)

    with col1:
        text = st.text_area(label="Enter your text", height=350, placeholder="Enter your text or article here")
        if st.button("Get Summary"):
            if text.strip():
                try:
                    summary = get_summary(text)
                    with col2:
                        st.write("Text Summary:")
                        st.code(summary)
                        st.write("Text Headline:")
                        st.code("Feature Coming Soon")
                except Exception as e:
                    st.error(f"An error occurred while generating the summary: {e}")
            else:
                st.warning("Please enter text to summarize!")

# News Summary and Headlines option
if choice == "News Summary and Headlines":
    st.title("BBC News Summary")
    search_query = st.text_input("Search for a topic", placeholder="Enter the topic you want to search")
    if st.button("Search News"):
        try:
            link_list, title_list, thumbnail_list = fetch_news_links(search_query)
            news_list = fetch_news(link_list)

            if link_list:
                col1, col2 = st.columns(2)
                for i, link in enumerate(link_list):
                    if i % 2 == 0:
                        with col1:
                            st.write(title_list[i])
                            with st.expander("Read The Summary"):
                                st.write(get_summary(news_list[i]))
                            st.markdown(f"[**Read Full Article**]({link})", unsafe_allow_html=True)
                    else:
                        with col2:
                            st.write(title_list[i])
                            with st.expander("Read The Summary"):
                                st.write(get_summary(news_list[i]))
                            st.markdown(f"[**Read Full Article**]({link})", unsafe_allow_html=True)
            else:
                st.info(f"No results found for '{search_query}'. Please try another keyword.")
        except Exception as e:
            st.error(f"An error occurred while fetching news: {e}")


# Input text from the user
user_text = st.text_input("Enter your text for tokenization:", "hello, this is Kishan Sai")

# Button to trigger evaluation
if st.button("Evaluate Tokenization Quality"):
    # Call the function from helper.py
    result = evaluate_tokenizer_quality(nlp, user_text)
    
    # Display the results
    st.write("Predicted Tokens:", result["Predicted Tokens"])
    st.write("Expected Tokens:", result["Expected Tokens"])
    st.write("Precision:", f"{result['Precision']:.2f}%")
    st.write("Recall:", f"{result['Recall']:.2f}%")
    st.write("F1-Score:", f"{result['F1-Score']:.2f}%")
