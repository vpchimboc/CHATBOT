import openai
openai.api_key = "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"

prompt = "Write a poem about a sunset"
model = "text-davinci-002"
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.5,
)
print(response.choices[0].text)