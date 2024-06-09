import os
from openai import OpenAI

# 设置OpenAI API密钥
client = OpenAI(
    # This is the default and can be omitted
    organization=os.getenv('OPENAI_ORGANIZATION'),
    project=os.getenv('OPENAI_PROJECT_ID'),
    api_key=os.getenv('OPENAI_API_KEY'),
)

# 请将此路径替换为实际的文件夹路径
folder_path = r"/Users/yikangsun/Google Drive/2024/2024_YIKANG_DOCS/Digital human in livestream selling"
# folder_path = r"/Users/yikangsun/Google Drive/2024/2024_YIKANG_VIDEOS/audio"


def read_files_in_folder(folder_path):
    files_content = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        print(filename)
        print(file_path)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
                content = file.read()
                files_content.append(content)
    return files_content


def summarize_content(content_list):
    combined_content = "\n".join(content_list)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是一个有帮助的助手。"},
            {
                "role": "user",
                "content": f"请基于以下内容写一个总结：\n{combined_content}",
            },
        ],
    )
    return response.choices[0].message.content


def main(folder_path):
    # 读取文件夹中的所有文件内容
    files_content = read_files_in_folder(folder_path)
    print(files_content)
    # 基于内容生成总结
    summary = summarize_content(files_content)
    print("======== 总结内容 ========\n")
    print(summary)

if __name__ == "__main__":
    main(folder_path)



