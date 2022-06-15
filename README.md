Projekt realizowany w ramach kierunku studiów podyplomowych: 
TESTER AUTOMATYZUJĄCY W SELENIUM
na uczelni Akademia Leona Koźmińsiego w Warszawie 
Stacjonarnie
Kierownik studiów: Grzegorz Mazur
Wykładowca promotor: Karol Kolański

zastsowano page object pattern zgodnie z:
https://selenium-python.readthedocs.io/page-objects.html#test-case

Data Driven Test wykonany częściowo z pwoodu braku możliwości logowania użytwkonika, 
która zostanie rozwinięta w przyszłości. "chr_login_test_case-data" 
wypełnia pola typu <input> prostymi danymi i wykonuje operację onClick() na "Zaloguj"
Zasadnie na potrzeby wymagań dyplomu został wykluczony z suit testowego "run_testy.py"

Pozostałe pięć przypadków testowe sprawdząją UI, UX oraz drzewo Reac.Component i React DOM

Projekt powstał w sytemie Windows
potrzebny chromedriver.exe - ostatnia wersja w folderze webdrivers
Link do sterowników: https://sites.google.com/a/chromium.org/chromedriver/downloads

zgodnie z reqirements.txt:
selenium~=4.2.0

Projekt wykonany z:
pip 22.1.2 (python 3.9)
Python 3.9.1
Wersja 102.0.5005.115 (Oficjalna wersja) (64-bitowa)

uruchomienie: "run_testy.py"

----------------------
Dla systemu Linux:
Link do sterowników: https://sites.google.com/a/chromium.org/chromedriver/downloads

Konsola: 
pip installs packages
pip3 install selenium
sudo apt-get install chromium-chromedriver

tests.chrome_tests.base_test.py class BaseTest
        # LINUX:
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://cabinternational.herokuapp.com")

----------------------
Specjalnie na potrzeby projektu równolegle zbudoway został sandbox 
w postaci szklieletu aplikacji webowej w technologi React z użyciam javascript
celem było przetestowanie możliwie nieprzyjaznych testerowi rozwiązań 
wygodnych dla forn-end developera oraz wad w oprogramowaniu, któe są trudno wykrywalne 
z perspektywy developera

Aplikacja Webowa w React to efekt wiedzy uzyskanej w ramach studiów podyplomowych 
Fornt-end Developer z React na Akademii Leona Koźmińskiego w roku akademickim 2020/2021
Pod kierownictwem: 
Grzegorz Mazur
Opiekun projektu zaliczeniowego w React: Rober Kuliński

w przyszłości oba projekty - testowy i webowy zostaną roziwnięte lub 
na nabytej na ich podstawie wiedzy rozwinięty zostanie projekt komercyjny

repozytorium: https://github.com/Pastor-git/cabinternational.git

----------------------
Oczekiwany rezultat dla "run_tests.py":

Ran 5 tests in 68.205s

FAILED (failures=1)

Test - "chhr_test_case#_reports.py" ma wykrywać symulowaną uproszcząną wadę w oprogramowaniu 
ujawniającą ścieżki dostępu na serwerze.

Pozostałe test powinnny zakończyć się pozytywnym rezultatem

----------------------
Dokumentacja:
wersja polskojęzyczna

chr_test_case1_counterbutton

        Testowanie wbudowanej funkcjonalności wewnątrz drugiej kompilacji przycisku z instancji React.Component CounterButton
        bez żadnych unikalnych właściwości - symulacja niewspierającego środowiska testera

        testowanie w przypadku, gdy każda instancja CounterButton jest niezależna i ma niezależny wynik oparty na „rekwizytach”
        bez ingerencji w stan danych button2.liczba powinna być wyższa niż nie kliknięty button1.number
        każdy lokalizator inny niż XPATH powinien prowadzić do wystąpienia CounterButton wyświetlanego jako pierwszy

chr_test_case2_menu



chr_test_case3_reports

chr_test_case4_author

chr_test_case5_logo