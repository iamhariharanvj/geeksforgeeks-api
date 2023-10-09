from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

def getScore(score):
    try:
        return int(score)
    except Exception:
        return 0

def getCount(text):
    pattern = r'\((\d+)\)'
    match = re.search(pattern, text)

    if match:
        return int(match.group(1))
    else:
        return 0

@app.route('/get/<username>', methods=['GET'])
def get_geeksforgeeks_data(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}"

    page = requests.get(url)

    if page.status_code != 200:
        return jsonify({"error": "User doesn't exist"})

    soup = BeautifulSoup(page.text, 'html.parser')

    scores = soup.find_all('span', class_="score_card_value")

    if len(scores) < 3:
        return jsonify({"error": "User doesn't exist"})

    data = dict()
    data["username"] = username
    data["overall_coding_score"] = getScore(scores[0].text)
    data["total_problems_solved"] = getScore(scores[1].text)
    data["monthly_coding_score"] = getScore(scores[2].text)

    data["problems"] = dict()

    problem_counts = soup.find_all('li', class_="tab")

    tags = ["school", "basic", "easy", "medium", "hard"]

    for i, tag in enumerate(tags):
        data["problems"][tag.lower()] = {"count": getCount(problem_counts[i].text)}
        data["problems"][tag.lower()]["problems"] = [
            {"question": problem.text, "link": problem.get('href')} for problem in soup.find('div', id=tag).find_all('a', href=True)]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
