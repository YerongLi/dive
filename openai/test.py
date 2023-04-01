# 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
import openai
openai.api_key = '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'
prompt = "The massive explosions destroyed vehicles on a highway just outside the base at the Syrian port-city of Tartus, northwestern Syria. It is understood the first blast was a car bomb planetout outside the base. The second explosion was a suicide bomber who detonated his belt as people rushedto help those injured, AFP reported. What is attacker in the sentence: The massive explosions destroyed vehicles on a highway just outside the base at the Syrian port-city of Tartus, northwestern Syria?"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)