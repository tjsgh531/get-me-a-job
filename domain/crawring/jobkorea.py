from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from tqdm import tqdm
import pandas as pd


class JobKorea():
    def __init__(self):
        ChromeDriverManager().install()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=duty")

    def select_fields(self):
        # 개발자 직군 클릭
        self. driver.find_element(By.XPATH, '//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]').click()

        # 개발자 직군 중 필요한 분야 선택
        fields_xpath = ['//*[@id="duty_step2_10031_ly"]/li[8]/label', '//*[@id="duty_step2_10031_ly"]/li[9]/label', '//*[@id="duty_step2_10031_ly"]/li[14]/label/span']

        for xpath in fields_xpath:
            self.driver.find_element(By.XPATH, xpath).click()
        else:
            self.driver.find_element(By.ID, 'dev-btn-search').click()

    def get_data(self):

        feature = []

        for i in tqdm(range(1, 26)):
            current_url = f"https://www.jobkorea.co.kr/recruit/joblist?menucode=duty#anchorGICnt_{i}"
            if self.driver.current_url != current_url:
                self.driver.get(current_url)
                time.sleep(3)

            items = self.driver.find_element(By.CLASS_NAME, 'tplList').find_elements(By.CLASS_NAME, 'devloopArea')

            for item in items:
                title = item.find_element(By.CLASS_NAME, 'tplCo')
                content = item.find_element(By.CLASS_NAME, 'tplTit')
                
                business_name = title.find_element(By.CLASS_NAME, 'link').text
                content_title = content.find_element(By.CLASS_NAME, 'link').text
                conditions = content.find_element(By.CLASS_NAME, 'etc').text
                try:
                    skills = [skill.strip() for skill in content.find_element(By.CLASS_NAME, 'dsc').text.split(',')]
                except NoSuchElementException:
                    skills = []
                    
                feature.append({
                    "business_name" :business_name,
                    "title" : content_title,
                    "coditions" : conditions,
                    "skills" : skills,
                })

        return pd.DataFrame(feature)