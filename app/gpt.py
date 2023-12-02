import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()

load_dotenv()

def get_destination(input):
    
    # print(input)

    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )

    response=client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0.2,
        top_p=0.5,
        max_tokens=2000,
        messages = [
            {"role": "system", "content":f"下記の文章から問題のみを抽出してください。出力は問題だけにして、他の文章は書かないでください。{input}"},
            {"role": "user","content": "抽出した問題と同じような問題を1つだけ作ってください。また、作った問題の解答を問題に続けて書いてください。問題と解答は*で囲ってください。出力は問題だけにして、他の文章は書かないでください。"}]
        )
    data=response.choices[0].message.content
    # return response
    dest = data.split("*")
    return dest
    # required_text = dest.openai[1]
    # print(required_text)
    
    # try:
    #     dest = data.split("*")
    #     return dest["openai"][1]

    # except IndexError as ex:
    #     print("説明: " + data)
    #     print("*****************")
    #     print("Don't worry : {}".format(ex))    
    #     return None