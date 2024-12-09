# Text Summarization Application

### Final project for CSCI 6660 - Artificial Intelligence

---

### Video Presentation:
A detailed video presentation on this project can be found here:  
[https://youtu.be/Yis-IlOYT0c]

---

### Goal:
Our objective was to create a web-based **Text Summarization Application** capable of intelligently summarizing text using NLP techniques. This includes summarizing both custom text inputs and news articles fetched from BBC News.  
We designed a scoring system to evaluate the summarization performance, leveraging tokenization accuracy and ROUGE scores to assess the quality of generated summaries.

**Key Features Implemented:**
1. Summarization of user-provided custom text.
2. News summarization using articles fetched with **NewsAPI**.
3. Evaluation metrics:
   - **Tokenization Accuracy**.
   - **Summarization Quality using ROUGE Scores**.

---

### Results:
After implementing and testing the application, the system demonstrated effective summarization capabilities for both user-provided text and fetched news articles. The evaluation metrics used are:

1. **Tokenization Accuracy**:  
   - Measures how well the text is split into words, punctuation, and other meaningful tokens.
   - Precision, Recall, and F1-score values highlight its performance.

2. **ROUGE Scores**:  
   - Evaluate the summarization quality by comparing generated summaries with reference summaries.  
   - Higher ROUGE-1, ROUGE-2, and ROUGE-L scores indicate better summarization performance.

The application performs well in generating concise summaries but may lose minor details due to summarization constraints.

---

### How-to-use:
After downloading the project files from the repository:
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
2. Run the three code files (main.py, helper.py, rouge.py) in the command line as needed:
    To start the main application: python main.py
    To test helper functions: python helper.py
    To calculate ROUGE scores independently: python rouge.py

Use the application for:
    Custom Text Summarization: Input your text to get a concise summary.
    News Summarization: Enter a topic to fetch and summarize BBC News articles.
    Evaluate Tokenization Quality: Input custom text and view precision, recall, and F1-score for tokenization.
