import pyautogui
import requests

from bs4 import BeautifulSoup


class webscrapping:

    
    def pegarDados():
        
        #Matricula = pyautogui()
        response = requests.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')

        soup = BeautifulSoup(response.text, 'html.parser')

        matriculas = soup.find_all('//*[@id="agenda-docente"]/table/tbody/tr[1]/td[2]')

        #matricula = soup.find_all('Matrícula')

        print(matriculas)
            
if __name__ ==  "__main__":
    webscrapping()
