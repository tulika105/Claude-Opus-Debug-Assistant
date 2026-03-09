# Claude-opus-debug-assistant

A CLI tool that takes any bug description and returns a structured debugging plan — root causes, reproduction steps, fixes, and prevention — powered by Claude Opus 4.6 with adaptive thinking.

> **Adaptive thinking** means Claude Opus 4.6 decides on its own how much reasoning to apply. Simple bugs get fast answers. Complex bugs — race conditions, memory leaks, agent state issues — trigger deeper internal reasoning before a response is generated. You only see the final output, but the quality difference on hard problems is significant.

---

## What it does

You describe a bug in plain English. The tool sends it to Claude Opus 4.6, which returns a structured plan covering:

1. Most likely root causes (ranked)
2. How to reproduce and diagnose it
3. Step-by-step fix
4. How to prevent it next time

Every session is automatically saved as a JSON file in the `sessions/` folder.

---

## This repo consists of

- `debug_assistant.py` — main script that takes your bug as input and returns a full debugging plan
- `requirements.txt` — dependencies needed to run the project
- `sessions/` — auto-generated folder that saves every query and response as a JSON file

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/tulika105/Claude-Opus-Debug-Assistant.git
cd Claude-Opus-Debug-Assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create a `.env` file**
```
ANTHROPIC_API_KEY=your_api_key_here
```

Get your API key from [console.anthropic.com](https://console.anthropic.com).

---

## Run

```bash
python debug_assistant.py
```

You will be prompted to describe your bug. That's it.

---

## Example

**Input:**
```
I built a multi-agent pipeline using LangGraph with three agents. The researcher 
fetches data and adds it to state but the summarizer agent runs on an empty state 
instead of reading what the researcher wrote.
```

**Output:**
```
1. Most likely root causes
   - State is not being returned correctly from the researcher node...

2. How to reproduce and diagnose it
   - Add a print statement after the researcher node runs...

3. Step-by-step fix
   - Make sure your node function returns the full updated state dict...

4. How to prevent it
   - Always define your state schema using TypedDict with Annotated reducers...
```

**Saved to:** `sessions/debug_20260309_143022.json`

---

## Stack

- Python 3.9+
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- Model: `claude-opus-4-6`
- Adaptive thinking enabled

---

## Why Claude Opus 4.6?

Opus 4.6 with adaptive thinking decides on its own when a problem needs deep reasoning and when it doesn't. For complex bugs like race conditions, agent state issues, or memory leaks it reasons through multiple hypotheses before responding — not just surface-level suggestions.

---
