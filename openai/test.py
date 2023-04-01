# 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
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
prompt = "Elliott said that McVeigh gave him the $280.32 in exact change after declining to pay an additional amount for insurance. \n Who is the buyer of this event?"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=20,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print(type(response))