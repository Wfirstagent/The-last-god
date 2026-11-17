#!/bin/bash
# 1. Check karo agar proxy pehle se chal rahi hai ya nahi, nahi toh start karo
if ! pgrep -f "proxy.py" > /dev/null; then
    python3 proxy.py &
    sleep 1
fi

# 2. Environment variables set karo (GitHub par secure rahega)
export ANTHROPIC_BASE_URL="http://localhost:8000/v1"
export ANTHROPIC_AUTH_TOKEN="${OPENROUTER_API_KEY}"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek/deepseek-chat"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek/deepseek-chat"

# 3. Claude Code launch karo
claude

