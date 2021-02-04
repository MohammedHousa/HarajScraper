import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# The URL for the targeted web sit
URL = 'https://haraj.com.sa/tags/%D8%A7%D8%B1%D8%A7%D8%B6%D9%8A%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9%20%D9%81%D9%8A%20%D8%AD%D9%8A%20%D8%A7%D8%A8%D8%AD%D8%B1%20%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D9%84%D9%8A%D8%A9%20%D9%81%D9%8A%20%D8%AC%D8%AF%D9%87'
page = requests.get(URL)

driver = webdriver.Firefox()
driver.get(URL)


def more_posts():
    button_element = driver.find_element_by_id('more')
    button_element.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def view_posts():
    soup = BeautifulSoup(driver.page_source, features="lxml")

    # Initial a variable to keep track of the number of posts
    post_id = 0

    # Accessing each post title on the page and getting there links
    post_title = soup.find_all('div', class_='postTitle')
    for post in post_title:
        post_id += 1
        post_url = 'https://haraj.com.sa' + post.a['href']
        page_post = requests.get(post_url)
        soup_post = BeautifulSoup(page_post.content, 'html.parser')

        # Printing the title of each post with it's ID numbers
        print(post_id, soup_post.find('h3').text, end='\n' * 2)

        # Accessing the posts body
        post_body = soup_post.find('div', class_='postBody')

        # Split the text into lines, each line in a list
        try:
            body_text = post_body.text.split('\n')

            # Remove the empty lines from the list
            while "" in body_text:
                body_text.remove("")

            # get rid of all the duplicate whitespaces and newline characters
            body_text = " ".join(str(body_text).split())

            # Replacing the ',' and '[]'
            print(body_text.replace(',', '\n').replace('[', '').replace(']', ''))

            # Getting and printing the time of each post
            post_header = soup_post.find('div', class_="postHeader")
            print('\n' + post_header.find('span').text)

            # Printing the URL of each post
            print(post_url, end='\n' * 2)
        except:
            # Printing the URL of each post
            print(post_url, end='\n' * 2)
            print("No post" + "\n" * 5)
    driver.close()
