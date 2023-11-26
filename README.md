# leaked
Python program that checks for data leakage when given a website/web app

This program uses the requests library to send HTTP requests to the web app and the BeautifulSoup library to parse HTML content. It defines a recursive function that crawls the web app and checks the response status codes for data leakage paths. It also follows the links in the HTML content and checks for data leakage in the subpages. It prints a warning message or a normal message for each URL accordingly.

To run this program, you need to have python installed on your computer and the requests and BeautifulSoup libraries installed using pip. You also need to change the web_app_url variable to the URL of the web app you want to check. Then, you can run the program from the command line or an IDE of your choice.
