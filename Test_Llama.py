"""
Testing Llama API/SDK

10 Nov 2023

To create a Python Virtual Environment:
a) To create the Python venv, go to Manage > Command Palette > Create Environment (.venv folder should appear in project root).
b) In Terminal type ".venv\Scripts\activate" (A green (.venv) should appear to the left of the Terminal prompt).

Get the key by going to 
https://huggingface.co
Creating an account
then creating a Pro account with your credit card
Click on your account (TRHC) blue orb > Settings > Access Tokens

Then in the Terminal type
    "setx OPENAI_API_KEY <the key>"
 
WARNING: You have to quit out of VS Code (this IDE) and go back in before the new system environment variables are avaliable

FYI: To see all system environment variables,
        go to the DOS COMMAND PROMPT and type "set"


Bad request:
Model requires a Pro subscription; check out hf.co/pricing to learn more. 
Make sure to include your HF token in your query.

"""
import os 
# pip install --upgrade easyllm
from easyllm.clients import huggingface

# helper to build llama2 prompt
# Changing configuration without using environment variables
huggingface.prompt_builder = "llama2"
huggingface.api_key = "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"

"""
Prompt Builder empowers you to enhance Salesforce out-of-the-box prompts or 
create your own prompt template that increases workforce productivity in the flow of work.
Wow!
"""

# set env for prompt builder
#os.environ["HUGGINGFACE_PROMPT"] = "llama2" # vicuna, wizardlm, stablebeluga, open_assistant
#os.environ["HUGGINGFACE_TOKEN"] = "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" 

response = huggingface.ChatCompletion.create(
    model="meta-llama/Llama-2-70b-chat-hf",
    messages=[
        {"role": "system", "content": "\nYou are a helpful assistant speaking like a pirate. argh!"},
        {"role": "user", "content": "What is the sun?"},
    ],
    temperature=0.9,
    top_p=0.6,
    max_tokens=256,
)

# print(response)
print(response['choices'][0]['message']['content'])


"""
{'id': 'hf-83kMqelvG1', 
'object': 'chat.completion', 
'created': 1699648612, 
'model': 'meta-llama/Llama-2-70b-chat-hf', 
'choices': [{'index': 0, 'message': {'role': 'assistant', 

'content': '  Arrrr, the sun be a big ol\' ball o\' fire in the sky, me hearty! It be the source o\' light and warmth for our fair planet, 
and it be a mighty powerful force, savvy? Without the sun, we\'d be lost and adrift in the darkness, 
so let\'s give a hearty "Yarrr!" for the sun, the scurviest celestial body on the high seas of space! Arrrr!'}, 

'finish_reason': 'eos_token'}], 
'usage': {'prompt_tokens': 27, 'completion_tokens': 105, 'total_tokens': 132}}

"""


