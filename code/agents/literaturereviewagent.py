import os
from openai import OpenAI
from openai import OpenAIError

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
        # only allow pdf and docx file
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    files_content.append(content)
    return files_content

# Function to split text into chunks
def split_text(chunks, text, max_tokens=8000):
    words = text.split()
    chunk = []
    chunk_size = 0

    for word in words:
        word_size = len(word) + 1  # Adding 1 for the space
        if chunk_size + word_size <= max_tokens:
            chunk.append(word)
            chunk_size += word_size
        else:
            chunks.append(" ".join(chunk))
            chunk = [word]
            chunk_size = word_size
    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

def split_files_to_chunks(files_content):
    chunks = []
    for file_text in files_content:
        split_text(chunks, file_text)
    return chunks

def call_openai_api(chunk):
    size = len(chunk);
    print("process chunk with size: " + str(size)) 
    try:        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chunk}
            ]
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        print(f"An error occurred: {e}")
        return ""

def summarize_content(chunks):
    responses = []
    index = 0
    for chunk in chunks:
        response = call_openai_api(chunk)
        responses.append(response)
        index += 1
        print("processed to index: " + str(index))

    # Combine the responses if necessary
    final_response = " ".join(responses)
    return final_response


def main(folder_path):
    # 读取文件夹中的所有文件内容
    files_content = read_files_in_folder(folder_path)
    
    # split to chunks
    chunks = split_files_to_chunks(files_content)
    print("chunks' length is: " + str(len(chunks)))

    # 基于内容生成总结
    summary = summarize_content(chunks)
    print("======== 总结内容 ========\n")
    print(summary)

if __name__ == "__main__":
    main(folder_path)



