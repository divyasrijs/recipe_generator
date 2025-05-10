import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client('YOUR_API_KEY')  # Replace with your actual key

# Function to generate recipes
def get_recipe(ingredients):
    # Use the Cohere API to generate the recipe
    response = co.generate(
        model='command-r-plus',  # Use 'command-r' or 'command-r-plus' as available
        prompt=f'Give me a recipe using {ingredients}.',
        max_tokens=500  # Adjust the token length as needed
    )
    
    # Access the generated text from the response
    return response.generations[0].text.strip()

# Streamlit app UI
st.title("AI Recipe Generator")

# Input ingredients from the user
ingredients = st.text_input("Enter the ingredients (comma-separated):")

if ingredients:
    # Get recipe suggestion from Cohere API
    recipe = get_recipe(ingredients)

    # Display the generated recipe
    st.subheader("Recipe Suggestion:")
    st.write(recipe)
else:
    st.info("Please enter ingredients to get a recipe suggestion.")
