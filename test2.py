import os
import openai
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "the following is a conversation with an AI assistant."
def gpt_output(prompt):
 response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens = 150,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0.6,
    stop = ["Human:", "AI:"]
    )
 print("AI Response :", response.choices[0].text)

#gpt_output("who is the father of ai")

while True:
    query = input("ask a question to AI : \n")
    gpt_output(query)