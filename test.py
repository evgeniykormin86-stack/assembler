from langchain_openai import OpenAIEmbeddings



# Set your OpenRouter API key in environment variables:
# export OPENAI_API_KEY="YOUR_OPENROUTER_KEY"

embeddings = OpenAIEmbeddings(
    model="openrouter-gpt4",  # or whichever embedding model OpenRouter supports
    api_key="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"
)

vector = embeddings.embed_query("Hello world")
print(vector)

