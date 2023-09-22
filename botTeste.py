def bot():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    import tkinter as tk
    import time
    from selenium.webdriver.common.action_chains import ActionChains

    root = tk.Tk()
    root.withdraw()
    caminho_chromedriver = 'C:/Users/win/Desktop/CHROME DRIVER/chromedriver.exe'
    driver = webdriver.Chrome()
    options = Options()
    options.add_experimental_option("detach", True)
    driver.get("http://minibit.com.br/arquivosbot/WAPI_BETA.js")
    script = driver.find_element(By.CSS_SELECTOR, "body > pre").text
    driver.get("https://web.whatsapp.com/")
    input("Aperte enter após ler o QR code.")
    driver.execute_script(script)
    time.sleep(1)
                
    while True:
        try:
            mensagen = driver.find_element(By.CSS_SELECTOR, '[aria-label="Não lidas"]')
            if mensagen:
                mensagen.click()
                first = False
            
            teste = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/span/span')
            prompt = teste.text
            import ArvoreDeDecisao as choose
            from selenium.webdriver.common.keys import Keys
            resposta = choose.decisoes.choose(prompt)
            # Crie uma instância de ActionChains
            actions = ActionChains(driver)
            if resposta != "":
                actions.send_keys(resposta)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                
                actions.send_keys(Keys.ESCAPE)
                actions.perform()
                resposta = ""
                prompt = ""
            else:
                actions.send_keys("eita")
            actions.perform()

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # Espere um curto período antes de verificar novamente (evite sobrecarregar o navegador)
        time.sleep(2)
