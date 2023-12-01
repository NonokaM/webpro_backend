from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()

load_dotenv()

def get_destination():

    client = OpenAI(
        # api_key=os.environ['OPENAI_API_KEY'],
        api_key="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"
    )

    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        top_p=0.5,
        messages=[
            {"role": "system", "content": "あなたは大学生の家庭教師です。"},
            {"role": "user", "content": "OSに関する問題を考えて。"}
        ]
    )

    data = response

    try:
        print(data)
        return data
    except:
        print("error")
        return "error"
