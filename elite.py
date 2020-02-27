from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time

#ABRIR PAINEL
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path="chromedriver", chrome_options=option)

browser.get("https://pumbacms.com:8443/login")

time.sleep(5)

#LOGAR NO PAINEL
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="botaoLogin2"]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

input_login = browser.find_elements_by_xpath('//*[@id="LoginForm"]/div[1]/input')[0]
input_login.clear()
input_login.send_keys("mateusc")

input_password = browser.find_elements_by_xpath('//*[@id="LoginForm"]/div[2]/input')[0]
input_password.clear()
input_password.send_keys("Mm130691")

button_login = browser.find_elements_by_xpath('//*[@id="botaoLogin2"]')[0]
button_login.click()

#ABRIR PAGINA DE CLIENTES
browser.get("https://pumbacms.com:8443/clientes")
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1742992"]/td[3]')))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()



filtrar_clientes = browser.find_elements_by_xpath('//*[@id="costumers"]/thead/tr/th[7]')[0]
filtrar_clientes.click()


abrir_dropdown = browser.find_elements_by_xpath('//*[@id="costumers_length"]/label/select')[0]
abrir_dropdown.click()
selecionar_todos_clientes = browser.find_elements_by_xpath('//*[@id="costumers_length"]/label/select/option[4]')[0]
selecionar_todos_clientes.click()
abrir_dropdown = browser.find_elements_by_xpath('//*[@id="costumers_length"]/label/select')[0]
abrir_dropdown.click()







#CRIAR TESTE
# input_login_test = browser.find_elements_by_xpath('//*[@id="editarcliente"]/div[1]/div[2]/input')[0]
# input_login_test.clear()
# input_login_test.send_keys("test123")

# input_senha_test = browser.find_elements_by_xpath('//*[@id="editarcliente"]/div[1]/div[3]/input')[0]
# input_senha_test.clear()
# input_senha_test.send_keys("senha123")

# selecionar_plano = browser.find_elements_by_xpath('//*[@id="multiselect"]/option[1]')[0]
# selecionar_plano.click()
# button_plano = browser.find_elements_by_xpath('//*[@id="multiselect_rightSelected"]')[0]
# button_plano.click()

# button_criar_teste = browser.find_elements_by_xpath('//*[@id="validateButton"]')[0]
# button_criar_teste.click()

time.sleep(15)
browser.quit()


