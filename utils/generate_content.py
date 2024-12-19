from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Preprocess the user input
def preprocess_prompt(prompt):
    """
    Preprocesses the input prompt for content generation.
    Adds guiding instructions for the model.
    """
    prompt = prompt.strip().capitalize()  # Clean and format the input
    preprocessed_prompt = f"Tell me about {prompt} in an engaging blog post format with a title , paragraphs and as much accurate information as possible"
    return generate_content(preprocessed_prompt)

# Generate content based on the preprocessed input
def generate_content(prompt):
    """
    Generates text using T5 based on the given prompt.
    """
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large").to("cuda")  # Move model to GPU
    tokenizer.pad_token = tokenizer.eos_token  # Set padding token

    # Tokenize the input and move tensors to GPU
    inputs = tokenizer(prompt, return_tensors="pt", padding=True).to("cuda")
    
    # Generate text
    output = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_length=500,
        temperature=0.2,
        top_k=100,
        top_p=0.95,
        repetition_penalty=1.5,
        do_sample=True,
        no_repeat_ngram_size=3  # Prevent repeating 3-word sequences
    )

    # Decode and return the output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Check for repetitions
    if generated_text.count(prompt) > 2:
        return "The model generated repetitive content. Please refine your input."

    return generated_text

