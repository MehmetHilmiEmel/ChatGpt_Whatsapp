import os
import openai
from  API_KEY import API
openai.api_key = API.api_key

def model(text):
    repsonse=openai.Completion.create(
        model="curie:ft-personal:youtube-hilmi-2023-05-07-13-21-08",
        prompt="Cevaplar türkçe olsun. \n\nİnsan:"+text+"\nAI:",
        temperature=0.9,
        max_tokens=15,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" İnsan:", " AI:"]
        )

    print(repsonse["choices"][0]["text"])   

prompt=""

print(model("selam naber"))
# while True:
    
#     print("Enter Message")
#     x=input()