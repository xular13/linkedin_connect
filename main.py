from random import randint
import os
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

def main(maxConnect, Keywords = 'Data%20analyst'):
    login = 'login'
    passkey = 'your password'
    print('\nSigning in... (Takes about 10 seconds)')


    driver = webdriver.Chrome()
    
    # Opening LinkedIn Signinpage
    urltoSignInPage = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    driver.get(urltoSignInPage)
    time.sleep(2)

    # Logging in
    username = driver.find_element(By.XPATH, "//input[@name='session_key']")
    password = driver.find_element(By.XPATH,"//input[@name='session_password']")

    username.send_keys(login)
    password.send_keys(passkey)
    time.sleep(2)
    submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # Login Process Complete.
    os.system('cls||clear')
    print('\nSuccessfully signed in!')
    print()
    
    i = 0
    k = 1
    print("\nBeginning connection request process...\nThere is a delay between requests intentionally to bypass bot detections")
    while i < maxConnect:
        try:
            # Construct the URL for the search results page
            urllink = f"https://www.linkedin.com/search/results/people/?&keywords={Keywords}&network=%5B%22S%22%2C%22O%22%5D&origin=SWITCH_SEARCH_VERTICAL&page={k}&sid=aiC&spellCorrectionEnabled=true"
            
            # Load the search results page and wait for it to load
            driver.get(urllink)
            time.sleep(randint(4, 15))

            # Find all the Connect buttons on the page
            all_buttons = driver.find_elements(By.TAG_NAME, "button")
            connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

            # Loop through all the Connect buttons and send connection requests
            for btn in connect_buttons:
                driver.execute_script("arguments[0].click();", btn)
                name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/p/span/strong").text
                print(f"Sending connection request to {name}")
                time.sleep(randint(4, 15))
                send = driver.find_element(By.XPATH, "//button[@aria-label='Send without a note']")
                driver.execute_script("arguments[0].click();", send)
                time.sleep(2)
                i += 1
                if i >= maxConnect:
                    break 

            k += 1

            # Print the total number of connection requests sent so far
            print(f"Connection Invitations sent = {i}")
            time.sleep(randint(4, 15))

            # Exit the loop if the maximum number of connections has been reached
            if i >= maxConnect:
                break

    # Handle any exceptions that may arise during the process
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    print('Finished')




if __name__ == "__main__":
    keywords = input('Keywords for search (Press Enter for Data Analyst)')
    keywords = keywords.strip().replace(" ", '%20')
    try:
        maxConnect = int(input('\nHow many connection requests would you like to send? (Stay below 50 to be safe): '))
    except ValueError:
        maxConnect = 10
    if keywords == '':
        main(maxConnect)
    else:
        main(maxConnect, keywords)
        