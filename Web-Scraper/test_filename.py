# rule : save filename with test_*.py or *_test.py
# change the directory and type pytest in terminal
# cd Web-Scraper/My-Project/Demo_web_scraping/PyTest
# kate@kate-lappy:~/Desktop/Web-Scraper/My-Project/Demo_web_scraping/PyTest$ pytest

def test_isequal():
    x = 5
    y = 5
    assert x==y    

def test_check():
    name="Kate"
    title="Kate never give up"
    assert name in title

def test_check1():
    name = "kate"
    title = "kate is brave"
    assert name in title, "Title does not match"

def test_login():
    print("Login to app")

def test_checkout():
    print("checkout")

def test_logout():
    print("Logout from app") 

def f():
    return 10
def test_function():
    assert f() == 10           

    