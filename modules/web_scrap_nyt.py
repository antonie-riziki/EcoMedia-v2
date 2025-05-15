import requests as req
import envs



"""
High Level API to access New York Times news from the official NYTimes API.
The API only supports extraction of the most prominent lead-paragraph.
"""


load_dotenv()

NYT_API_KEY = os.environ.get("NYT_API_KEY")


base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'  

def get_response( news_topic) -> list:
    """
    Fetches the news.
    :param news_topic: supports news_topic and urls
    :return: abstract + description + lead_paragraph
    """
    url = f'{base_url}?q={news_topic}&api-key={NYT_API_KEY}'
    response = req.get(url).json()
    if 'response' in response and 'docs' in response['response']:
        docs = response['response']['docs']
        print(docs)
        abstract = docs[0].get('abstract', '')
        snippet = docs[0].get('snippet', '')
        lead_paragraph = docs[0].get('lead_paragraph', '')
        result = abstract + ' ' + snippet + ' ' + lead_paragraph
        return result
    return []


if __name__ == "__main__":
nytimes_api = NYTimesAPI()

# Specify the keyword for the article search
keyword = 'https://theathletic.com/5186510/2024/01/09/brian-flores-vikings-nfl-coaching-lawsuit/'

# Get and print the concatenated information from the response

concatenated_info = nytimes_api.get_response(keyword)
if concatenated_info:
    print(concatenated_info)
else:
    print("No response or invalid response format.")