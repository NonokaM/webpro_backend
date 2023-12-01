import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()

load_dotenv()

def get_destination():

    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )

    response=client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0.5,
        top_p=0.5,
        messages=[
            {"role": "system", "content": "あなたは大学生の家庭教師です。"},
            {"role": "user", "content": "OSに関する簡単な問題を一つ考えて。"}
        ]
    )

    data = response

    try:
        print(data)
        return data
    except:
        print("error")
        return "error"
