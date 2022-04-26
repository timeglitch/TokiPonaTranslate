import config
#load api key
APIKEY = config.SECRET_KEY

import os
import openai

openai.api_key= APIKEY
openai.organization = "org-qNYVl0J71153owejeurZzzCm"

listofengines = openai.Engine.list()

openai.Completion.create(
  engine="text-davinci-002",
  prompt="Say this is a test",
  max_tokens=5
)




