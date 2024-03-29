import ollama

# response = ollama.chat(
#     model="dolphin-mistral",
#     messages=[
#         {
#             "role": "user",
#             "content": "Why is the sky blue?",
#         },
#     ],
# )
messages = [
    {
        "role": "user",
        "content": "Why is the sky blue?",
    },
]
for chunk in ollama.chat("mistral:7b-instruct-v0.2-q8_0", messages=messages, stream=True):
    print(chunk["message"]["content"], end="", flush=True)
# print(response["message"]["content"])
