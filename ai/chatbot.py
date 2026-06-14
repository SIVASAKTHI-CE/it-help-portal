import httpx

OLLAMA_HOST = "host-gateway"
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

SYSTEM_PROMPT = """You are an IT helpdesk assistant for BITLA-ITDESK.
You help with: CrowdStrike Falcon installation, Zscaler setup,
Ubuntu/Windows issues, network troubleshooting, and general IT support.
Be concise, technical, and give step-by-step answers."""

async def ask_helpdesk(question: str) -> str:
    payload = {
        "model": "llama3.2:1b",
        "prompt": f"System: {SYSTEM_PROMPT}\n\nUser: {question}\nAssistant:",
        "stream": False
    }
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(OLLAMA_URL, json=payload)
        return resp.json()["response"]
