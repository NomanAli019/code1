from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import threading
import asyncio
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import autoit
import pyautogui 


from selenium.common.exceptions import WebDriverException
import time


async def videoplayer(url , ip_chan):
    max_retries = 5
    retries = 0
    while True:
        try:
            
            options = webdriver.ChromeOptions()
            path_to_extension = r'C:\Users\pc\Downloads\extension_3_80_5_0.crx'
            options.add_extension(path_to_extension)
            driver = webdriver.Chrome(options=options)
            # pyautogui.click(x=100 , y=100)
            # time.sleep(2)
            # pyautogui.moveTo(825,64)
            pyautogui.click(x=825 , y=64)
            time.sleep(2)
            # pyautogui.moveTo(700,220)
            pyautogui.click(x=700 , y=220)
            time.sleep(2)
            # pyautogui.moveTo(700,390)
            pyautogui.click(x=700 , y=390)
            time.sleep(2)
            pyautogui.click(x=700 , y=390)
            time.sleep(2)
            country_change = int(ip_chan)
            y_axis = 390-country_change
            pyautogui.click(x=700 , y=y_axis)
            # pyautogui.click(x=700 , y=y_axis)
            await asyncio.sleep(2)
            time.sleep(6)
            driver.get(url)
            time.sleep(5)

            play_btn = driver.find_element(By.CLASS_NAME, 'ytp-play-button')
            play_btn.click()
            skip_btn = driver.find_element(By.CLASS_NAME, 'ytp-ad-skip-button')
            
            if skip_btn:
                skip_btn.click()
                play_btn.click()
                time.sleep(50)
                driver.quit()

                break

            elif play_btn:
                play_btn.click()
                time.sleep(50)
                driver.quit()
                        
                break



        except WebDriverException as e:
            print(f"Caught WebDriverException: {str(e)}")
            print("no adds found in this video ")
            try: 
                if play_btn != None:
                    play_btn.click()
                    time.sleep(50)
                    driver.quit()
                    
                    break
            except UnboundLocalError:
                retries += 1
                if retries >= max_retries:
                    print(f"Max retries reached ({max_retries}). Exiting.")
                    break
    

async def main():
    Ip_Changer = [145,110,70]
    urls = ["https://youtu.be/EJYov0hBSYg?feature=shared","https://youtu.be/ClYj50yGzIk?feature=shared", "https://youtu.be/slJgccFBQu8?feature=shared"]
    threads =[]
    i = 0
    tasks =[]
    for url in urls:
        ip_chan = Ip_Changer[i] 
        i += 1
        task = asyncio.create_task(videoplayer(url,ip_chan))
        # threads.append(thread)
        tasks.append(task)
        # thread.start()
        # time.sleep(5)

    await asyncio.gather(*tasks)

    for thread in threads:
        thread.join()



    # videoplayer(url)

if __name__ == "__main__":
    asyncio.run(main())