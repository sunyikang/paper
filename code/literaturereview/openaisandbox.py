import os
from openai import OpenAI

# export OPENAI_API_KEY="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"
# export OPENAI_PROJECT_ID="proj_mRGIs9hHJz9uFCbunHj8xIHx"

print(os.getenv('OPENAI_PROJECT_ID'))
print(os.getenv('OPENAI_API_KEY'))

client = OpenAI(
    # This is the default and can be omitted
    organization='org-jqpcCgmVU2S09JEQeCFbwIV7',
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
    model="gpt-3.5-turbo",
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

