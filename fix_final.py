import json

with open('data.json', 'r') as f:
    data = json.load(f)

# Pehla working provider utha rahe hain
p = data.get('providers', [])[0]
base_url = p.get('baseUrl')
model_id = p.get('models', [{}])[0].get('id', 'deepseek/deepseek-chat')

print(f"URL: {base_url}")
print(f"Model: {model_id}")

with open('claude_env.sh', 'w') as f:
    f.write(f'export ANTHROPIC_BASE_URL="{base_url}"\n')
    f.write(f'export ANTHROPIC_DEFAULT_SONNET_MODEL="{model_id}"\n')
    f.write(f'export ANTHROPIC_DEFAULT_OPUS_MODEL="{model_id}"\n')
    f.write('export ANTHROPIC_API_KEY="free-token"\n')
