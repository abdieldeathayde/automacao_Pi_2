import requests

# Send a Get request to the URL

response = requests.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')


print(response.text)

#print