from chalicelib.article_parser import parser
from chalice import Chalice
import boto3

app = Chalice(app_name='treng')
client = boto3.client('translate')


@app.route('/', methods=['POST', 'GET'])
def index():
    if app.current_request.method == 'GET':
        return {'hello': "Yo!"}

    elif app.current_request.method == 'POST':
        body = app.current_request.json_body
        article = parser(body['url'])
        if article.text != '':
            response = client.translate_text(
                Text=article.text,
                SourceLanguageCode='tr',
                TargetLanguageCode='en')
            article.translated_text = response["TranslatedText"]
            return article.__dict__
        else:
            return {"text": None}
