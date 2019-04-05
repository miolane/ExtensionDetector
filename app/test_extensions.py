from selenium import webdriver
import os
import time
#the directory where extensions are stored
file_dir = 'D:\Personal\Desktop\selenium\extensions'
for root, dirs, files in os.walk(file_dir):
    for file in files:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_extension(file_dir+'\\'+file)
        browser = webdriver.Chrome(
            executable_path="D:\Personal\Desktop\study\python\crawler\env\chromedriver.exe",
            chrome_options = chrome_options
        )
        browser.get('file:///G:/html/webgl/index.html')
        time.sleep(2) #wait for all loaded
        # some extensions may pop and switch to a new tab, we need to switch back
        handles = browser.window_handles
        if len(handles) > 1:
            browser.switch_to_window(handles[0])
            time.sleep(10)
        else
            time.sleep(8)
        browser.quit()
