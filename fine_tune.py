import os
import openai
from  API_KEY import API
openai.api_key = API.api_key

respond=openai.FineTune.retrieve(id="ft-gISACZ6JW4j6oaJ1Qr2Za4Ky")

print(respond)
# file-t1AhEVvhUgv1oL9r1UV9kJ2r

# ft-gISACZ6JW4j6oaJ1Qr2Za4Ky
