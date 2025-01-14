from transformers import pipeline

# Initialize the QA pipeline using a pre-trained model
qa_pipeline = pipeline("question-answering")

def get_answer(context, question):
    """
    Uses a pre-trained transformer model to find an answer to a given question based on the provided context.
    
    :param context: The context text where the answer will be found.
    :param question: The question to be answered.
    :return: The answer to the question based on the context.
    """
    # Create the input dictionary for the pipeline
    input_data = {
        "context": context,
        "question": question
    }
    
    # Get the answer from the QA model
    result = qa_pipeline(input_data)
    
    return result['answer']

# Example usage
context_text = """
Recycling is the process of converting waste materials into new products to prevent waste of potentially useful materials. 
It is important for reducing the consumption of fresh raw materials, reducing energy usage, lowering greenhouse gas emissions, 
and reducing air and water pollution.
"""
question_text = "Why is recycling important?"

answer = get_answer(context_text, question_text)
print(f"Answer: {answer}")
