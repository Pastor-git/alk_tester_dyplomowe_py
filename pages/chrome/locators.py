from selenium.webdriver.common.by import By


class Home_Page_Locators():
    TEST_BUTTON = (By.ID, "testbutton")
    SECOND_BUTTON = (By.XPATH, "/html/body/div/div[2]/div[2]/button")
    MAIN_DIV = (By.XPATH, "/html/body/div[1]/nav")
    HOME_PAGE_BUTTON = (By.XPATH, "/html/body/div[1]/nav/table/tr[1]/a/button")
    REPORTS_PAGE_BUTTON = (By.XPATH, "/html/body/div[1]/nav/table/tr[2]/a/button")
    ARTICLES_PAGE_BUTTON = (By.XPATH, "/html/body/div[1]/nav/table/tr[3]/a/button")
    LOGO = (By.XPATH, "/html/body/div[1]/div[1]/img")

class Report_Page_Locators():
    REPORT = (By.CLASS_NAME, "report")

class Articles_Page_Locators():
    ARTICLE = (By.CLASS_NAME, "article")