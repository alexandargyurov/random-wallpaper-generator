import urllib.request
import random
from unsplash.api import Api
from unsplash.auth import Auth

client_id = "unsplashed_api_id"
client_secret = "unsplashed_secret_key"
redirect_uri = "localhost"

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)
for x in range(4):
    photo = api.photo.get(api.photo.random(query='mountains', w=3840, count=1)[random.randint(0, len(api.photo.random(query='mountains', w=3840, count=1))-1)].id)

    def downloader(image_url):
        full_file_name = 'wallpaper' + str(x) + '.jpg'
        urllib.request.urlretrieve(image_url, full_file_name)


    downloader('https://unsplash.com/photos/' + photo.id + '/download')
