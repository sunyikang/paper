import os
from openai import OpenAI

# How to input the ENVIRONMENT into mac:
# 1 (open file)
# nano ~/.bash_profile
# 2 (add below context)
# export OPENAI_ORGANIZATION="org-jqpcCgmVU2S09JEQeCFbwIV7"
# export OPENAI_PROJECT_ID="proj_mRGIs9hHJz9uFCbunHj8xIHx"
# export OPENAI_API_KEY="sk-proj-GbQFFJ70XS1erfQotTKkT3BlbkFJkKr9O9TK96Hm5jAJxjtE"
# 3 (execute)
# source ~/.bash_profile

print(os.getenv('OPENAI_ORGANIZATION'))
print(os.getenv('OPENAI_PROJECT_ID'))
print(os.getenv('OPENAI_API_KEY'))

client = OpenAI(
    # This is the default and can be omitted
    organization=os.getenv('OPENAI_ORGANIZATION'),
    project=os.getenv('OPENAI_PROJECT_ID'),
    api_key=os.getenv('OPENAI_API_KEY'),
)

stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
print("\n\n")

# List all available models
models = client.models.list()
for model in models:
    print(model)

# make a simple query
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是一个有帮助的助手。"},
        {
            "role": "user",
            "content": f"请描述一下人类的觉知度近1000年的变化",
        },
    ],
)
summary = response.choices[0].message.content
print(summary)

