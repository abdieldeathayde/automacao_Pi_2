from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.service import Service
# chrome_options = Options()

# chrome_options.add_argument("--headless")

# p = caminho_do_web_driver
# driver = webdriver.Chrome(p + '\chromedriver.exe', options=chrome_options)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://sigaa.ifsc.edu.br/sigaa/public/home.jsf")

botao = navegador.find_element('xpath',
                               '//*[@id="acesso"]/ul/li[2]/a')
botao.click()

botao_login = navegador.find_element('xpath',
                                     '//*[@id="loginForm"]/table/tfoot/tr[2]/td/button')

botao_login.click()

matricula = navegador.find('xpath',
                      '//*[@id="agenda-docente"]/table/tbody/tr[1]/td[2]')
print(matricula.text)