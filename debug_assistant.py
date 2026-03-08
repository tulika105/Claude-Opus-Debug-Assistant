import os
import json
import datetime
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

bug = input("Describe your bug: ")

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    system="""You are a senior debugging engineer.

Cover these in order:
1. Most likely root causes (ranked)
2. How to reproduce and diagnose it
3. Step-by-step fix
4. How to prevent it

Be specific — real commands, real tools, no generic advice.""",
    thinking={"type": "adaptive"},
    messages=[
        {"role": "user", "content": bug}
    ]
)

answer = ""
for block in response.content:
    if block.type == "text":
        answer = block.text

print("\n--- Debugging Plan ---\n")
print(answer)

os.makedirs("sessions", exist_ok=True)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"sessions/debug_{timestamp}.json"

with open(filename, "w") as f:
    json.dump({"query": bug, "answer": answer, "timestamp": timestamp}, f, indent=2)

print(f"\n✅ Saved to {filename}")