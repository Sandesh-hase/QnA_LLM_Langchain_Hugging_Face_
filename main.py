from langchain.llms import OpenAI

import os

llm = OpenAI(open_api_key=os.environ['OPEN_API_KEY'], temperature=0.6)
text = "What is the capital of India"
print(llm.predict(text))


