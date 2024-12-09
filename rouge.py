from rouge_score import rouge_scorer

# Function to calculate ROUGE scores
def calculate_rouge(reference, generated_summary):
    """
    Calculate ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L) for a given reference summary and a generated summary.
    
    Parameters:
        reference (str): The reference summary (ground truth).
        generated_summary (str): The generated summary.
        
    Returns:
        dict: Dictionary containing ROUGE-1, ROUGE-2, and ROUGE-L scores.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, generated_summary)
    return {
        "ROUGE-1": scores['rouge1'].fmeasure,
        "ROUGE-2": scores['rouge2'].fmeasure,
        "ROUGE-L": scores['rougeL'].fmeasure
    }

# Example Usage
if __name__ == "__main__":
    # Reference summary (ground truth)
    reference_summary = "The quick brown fox jumps over the lazy dog."

    # Generated summary (from the summarization technique)
    generated_summary = "The brown fox jumps over a lazy dog."

    # Calculate ROUGE scores
    rouge_scores = calculate_rouge(reference_summary, generated_summary)

    # Print the scores
    print("ROUGE Scores:")
    for metric, score in rouge_scores.items():
        print(f"{metric}: {score:.4f}")
