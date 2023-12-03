import os
import re
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()

load_dotenv()

def val_result_data(data):
    pattern_double_quotes = r'「(.*?)」'
    pattern_square_brackets = r'~(.*?)~'
    data_q = re.findall(pattern_double_quotes, data)
    data_a = re.findall(pattern_square_brackets, data,re.DOTALL)
    return data_q,data_a

def get_destination(input):
    

    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )

    response=client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0.1,
        top_p=0.5,
        max_tokens=2000,
        messages = [
            {"role": "system", "content": "あなたは大学の教授です。問題作成の役割を担っています。問題数は四つにしてください。"},
            {"role": "user","content": f"下記の問題を元にして、新しい問題を作ってください。問題には'「」'、解答には'~'でくくってください。{input}"}]
        )
    
    data=response.choices[0].message.content
    data_q,data_a=val_result_data(data)
    json={"quesion":[data_q],"answer":[data_a]}
    return json