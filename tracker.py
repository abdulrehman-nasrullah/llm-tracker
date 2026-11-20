import json
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

prompt = "What is an API? Answer in 10 words."


gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
g = gemini.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt)
g_text = g.text.strip()
g_in = g.usage_metadata.prompt_token_count
g_out = g.usage_metadata.candidates_token_count


groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
r = groq.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
)
q_text = r.choices[0].message.content.strip()
q_in = r.usage.prompt_tokens
q_out = r.usage.completion_tokens


g_cost = (g_in * 0.30 + g_out * 2.50) / 1000000
q_cost = (q_in * 0.59 + q_out * 0.79) / 1000000


print("GEMINI | GROQ")
print(g_text, "|", q_text)
print("Tokens in:", g_in, "|", "Tokens in:", q_in)
print("Tokens out:", g_out, "|", "Tokens out:", q_out)
print("Cost:", g_cost, "|", "Cost:", q_cost)


data = {
    "prompt": prompt,
    "gemini": {"reply": g_text, "input_tokens": g_in, "output_tokens": g_out, "cost_usd": g_cost},
    "groq": {"reply": q_text, "input_tokens": q_in, "output_tokens": q_out, "cost_usd": q_cost},
}
with open("results.json", "w") as f:
    json.dump(data, f, indent=2)