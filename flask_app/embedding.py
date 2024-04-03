import pandas as pd
from gensim.models import Word2Vec
import json

# Load the Excel file
df = pd.read_excel("C:/Users/sunda/OneDrive/Desktop/Naren/large-language-example-app/test2.xlsx")

# Concatenate all text columns into a single string
text = " ".join(df.apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1))

# Split the text into tokens
tokens = text.split()

# Create Word2Vec model
model = Word2Vec([tokens], min_count=1, vector_size=100)

# Create a dictionary to store the word embeddings
embedding_dict = {}

# Iterate over each word and its embedding in the Word2Vec model
for word in model.wv.index_to_key:
    embedding_dict[word] = model.wv[word].tolist()

# Save the embedding dictionary as JSON
with open("embedding_data.json", "w") as f:
    json.dump(embedding_dict, f)
