import json

with open('data.json', 'r') as f:
    data = json.load(f)

provider = data.get('providers', [])[0]
name = provider.get('name')
base_url = provider.get('baseUrl')
model = provider.get('models', [{}])[0].get('id')

print(f"=== Connected Free API ===")
print(f"Provider: {name}")
print(f"Base URL: {base_url}")
print(f"Model: {model}")

with open('free_env.sh', 'w') as f:
    f.write(f'export ANTHROPIC_BASE_URL="{base_url}"\n')
    f.write(f'export FREE_LLM_MODEL="{model}"\n')
