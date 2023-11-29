import openai
import json
from base64 import b64decode, b64encode

prompt = input('The prompt: ')
openai.api_key = 'API_KEY'

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256',
    response_format='url',  
)

print(json.dumps(response, indent=4))

with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['url'])
file_name = '-'.join(prompt.split(' '))

with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)
