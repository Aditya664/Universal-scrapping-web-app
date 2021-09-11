from bs4 import BeautifulSoup
import os
import functions
import requests
from flask import Flask, render_template, url_for, request
# result = requests.get("https://google.com")
# print(result.text)
# main fun.
# make http Request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    url = request.form["url"]
    result = main_function(url, "Test")
    return render_template("index.html", result=result)


def main_function(url, path):
    array = []
    functions.create_directory(path)
    sourcode = requests.get(url)
    sourcetext = sourcode.text
    soup = BeautifulSoup(sourcetext, "html.parser")
    divs = soup.find_all("div")
    a_tags = soup.find_all("a")
    h3_tags = soup.find_all("h3")
    h1_tags = soup.find_all("h1")
    img_tags = soup.find_all("img")
    p_tags = soup.find_all("p")

    for img_tag in img_tags:
        img_src = img_tag.get("src")
        obj = {'img_src': img_src}
        array.append(obj)

    for div in divs:
        div_text = div.text
        obj = {'div_text': div_text}
        array.append(obj)

    for a_tag in a_tags:
        a_href = a_tag.get("href")
        obj = {'a_href': a_href}
        array.append(obj)

    for h3_tag in h3_tags:
        h3_text = h3_tag.text
        obj = {'h3_text': h3_text}
        array.append(obj)

    for p_tag in p_tags:
        p_text = p_tag.text
        obj = {'p_text': p_tag.text}
        array.append(obj)

    return array


if __name__ == "__main__":
    app.run(debug=True)
