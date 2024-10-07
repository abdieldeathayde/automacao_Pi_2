import requests

from bs4 import BeautifulSoup

response = requests.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')

soup = BeautifulSoup(response.text, 'html.parser')

matriculas = soup.find('//*[@id="agenda-docente"]/table/tbody/tr[1]/td[2]')

#alerta = soup.find('')
#matricula = soup.find_all('Matrícula')





