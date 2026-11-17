import json

with open('data.json', 'r') as f:
    data = json.load(f)

# Aion Labs ya pehla working free provider select kar rahe hain
provider = data.get('providers', [])[0]
base_url = provider.get('baseUrl')
model_id = provider.get('models', [{}])[0].get('id')

print(f"🔗 Base URL: {base_url}")
print(f"🤖 Model ID: {model_id}")

with open('claude_env.sh', 'w') as f:
    f.write(f'export ANTHROPIC_BASE_URL="{base_url}"\n')
    f.write(f'export ANTHROPIC_DEFAULT_OPUS_MODEL="{model_id}"\n')
    f.write(f'export ANTHROPIC_DEFAULT_SONNET_MODEL="{model_id}"\n')
    f.write('export ANTHROPIC_API_KEY="free-bypass"\n')
