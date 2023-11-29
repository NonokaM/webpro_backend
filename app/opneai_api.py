from test import text_detection
from openai import OpenAI

text=text_detection()

client=OpenAI(
  api_key="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"
)
messages=[
    {"role":"user",
    "content":"f{text}あなたは大学教授で試験問題を作る役割を担当しています。上記の問題を元に類似の問題を作ってください。出力は問題だけにして、他の文章は書かないでください。"}
  ]

def generate_test():
  response =client.chat.completions.create(messages=messages,model="gpt-4-1106-preview",n=1,max_tokens=1000)
  print(response)
  return response