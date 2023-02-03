# Web scraping 

```python
from selenium import webdriver
PATH = "Path to web browser driver"

driver = webdriver.Chrome(PATH)
driver.get("url")
driver.close() # This will close the current tab
driver.quit() # This will close the entire browser
```

Locating elements from HTML
1. ID: this is a unique identifier of that element through out the whole html code.
2. Name: this is not necesarily unique.
3. Class: this is not unique and it will return the first match it can find.
```python
from selenium.webdriver.common.keys import Keys

search  = driver.find_element("")
search.send_keys("input you want to send")
search.send_keys(Keys.RETURN) # This simulates pressing the Enter key in the keyboard
```

### Explicit Waits
<br>
This is used to wait for the elements on the web browser to load before moving on to the next python command.
<br>
They allow your code to halt program execution, or freeze the thread, until the condition you pass it resolves. The condition is called with a certain frequency until the timeout of the wait is elapsed. This means that for as long as the condition returns a falsy value, it will keep trying and waiting.

```python

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


main = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID,"id you are searching")))

other_element = main.find_element("x")

```

### Implicit Waits
<br>
By implicitly waiting, WebDriver polls the DOM for a certain duration when trying to find any element. This can be useful when certain elements on the webpage are not available immediately and need some time to load.
<br>


```python
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")

```