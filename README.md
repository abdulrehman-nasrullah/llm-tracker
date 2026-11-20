# Gemini vs Groq

A small script that sends the same prompt to Gemini and Groq, then compares the reply, token usage and cost side by side.

I made this to see how two different providers answer the same question and how much each one would cost.

## What it does

- Sends one prompt ("What is an API? Answer in 10 words.") to both models
- Prints both replies next to each other
- Shows input and output tokens for each
- Calculates the cost in USD
- Saves everything in `results.json`

## Models used

- Gemini: `gemini-3.5-flash-lite`
- Groq: `openai/gpt-oss-120b`

## Setup

Install the packages:

```
pip install python-dotenv google-genai groq
```

Make a `.env` file in the same folder and add your keys:

```
GEMINI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

## Run

```
python main.py
```

(change `main.py` to whatever your file is named)

## Example output

```
GEMINI | GROQ
<gemini reply> | <groq reply>
Tokens in: ... | Tokens in: ...
Tokens out: ... | Tokens out: ...
Cost: ... | Cost: ...
```

A `results.json` file is also created with the same data.

## How the cost is calculated

Prices are per 1 million tokens:

| | Input | Output |
|---|---|---|
| Gemini | $0.30 | $2.50 |
| Groq | $0.59 | $0.79 |

Cost = (input tokens x input price + output tokens x output price) / 1,000,000

These prices are hardcoded in the script, so if the providers change their pricing you will have to update them yourself.

## Notes

- Don't upload your `.env` file to GitHub. Add it to `.gitignore`.
- To try a different question, just change the `prompt` variable at the top.