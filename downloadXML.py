from selenium import webdriver

browser = webdriver.Chrome()
browser.get(('http://is.hust.edu.vn/~phuongnh/thdl/'))

linksize = browser.find_elements_by_tag_name("a")
link = []
for x in linksize:
    link.append(x.get_attribute("href"))

for x in link:
    if x.endswith("docx") or x.endswith("doc"):
        browser.get(x)

download_dir="/home/wnncr/Downloads"
options = webdriver.ChromeOptions()
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],"download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)


for i in link:
    if i.endswith('pdf'):
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
        driver.get(i)

browser.close()
driver.close()
