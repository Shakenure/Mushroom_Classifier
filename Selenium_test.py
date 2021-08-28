from selenium import webdriver
import time
import pytest

class TestMushroom:
    
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
            
    def test_homepage(self,setup): 
        self.driver.get("http://127.0.0.1:8000")
        bt1 =self.driver.find_element_by_xpath("/html/body/div[1]/button/span/a")
        time.sleep(3)
        bt1.click()
        time.sleep(5)
        assert self.driver.title=="naiveBayes"
    
    def test_1(self,setup):
        self.driver.get("http://127.0.0.1:8000/naiveBayes/")        
        self.driver.find_element_by_name("CapShape").click()
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[4]/select/option[5]").click()
        
        time.sleep(2)
        self.driver.find_element_by_name("CapColor").click()
        self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[1]/select/option[8]").click()        
        time.sleep(2)
        self.driver.find_element_by_id("Predict").click()
        time.sleep(2)                
        assert self.driver.find_element_by_tag_name('body').text=="Edible"
   
    def test_2(self,setup):
        
        self.driver.get("http://127.0.0.1:8000/naiveBayes/")        
        self.driver.find_element_by_name("CapSurface").click()
        
        self.driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div[1]/select/option[2]").click()
        
        time.sleep(1)
        self.driver.find_element_by_name("Bruises").click()
        self.driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div[4]/select/option[3]").click()        
        time.sleep(2)
        self.driver.find_element_by_id("Predict").click()
        time.sleep(2)                
        assert self.driver.find_element_by_tag_name('body').text=="Edible"
    
     
     
        def test_3(self,setup):
        
        self.driver.get("http://127.0.0.1:8000/naiveBayes/")        
        self.driver.find_element_by_name("Odor").click()
        
        self.driver.find_element_by_xpath("/html/body/form/div[4]/div[2]/div[1]/select/option[4]").click()
        
        time.sleep(1)
        self.driver.find_element_by_name("GillAttachment").click()
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[1]/select/option[3]").click()        
        time.sleep(2)
        self.driver.find_element_by_name("GillSpacing").click()
        self.driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[2]/select/option[2]").click()        
        time.sleep(2)
        
        self.driver.find_element_by_id("Predict").click()
        time.sleep(2)                
        assert self.driver.find_element_by_tag_name('body').text=="Poisonous"
     
        
        def test_4(self,setup):
            self.driver.get("http://127.0.0.1:8000/naiveBayes/")        
        
            self.driver.find_element_by_name("GillSize").click()
            
            self.driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[3]/select/option[2]").click()
            
            time.sleep(1)
            self.driver.find_element_by_name("GillColor").click()
            self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[2]/select/option[9]").click()        
            time.sleep(2)
            self.driver.find_element_by_name("StalkShape").click()
            self.driver.find_element_by_xpath("/html/body/form[1]/div[7]/select/option[2]").click()        
            time.sleep(2)
            
            self.driver.find_element_by_id("Predict").click()
            time.sleep(2)                
            assert self.driver.find_element_by_tag_name('body').text=="Poisonous"
         
            
    '''    
driver=webdriver.Chrome("chromedriver.exe")
driver.get("http://127.0.0.1:8000/naiveBayes/")

time.sleep(5)
driver.find_element_by_name("CapColor").click()
driver.find_element_by_xpath("/html/body/form[1]/div[3]/select/option[8]").click()


driver.get_screenshot_as_file("ss1.png") 

driver.find_element_by_id("Predict").click()

time.sleep(5)
print(driver.find_element_by_tag_name('body').text=="Edible")
driver.quit()

'''