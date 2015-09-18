from twython import TwythonStreamer
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        #self.disconnect()

    def on_error(self, status_code, data):
        print "Error!!", status_code, data

		
url = "https://stream.twitter.com/1.1/statuses/sample.json?delimited=length"
# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(api_key, api_secret,
                    access_token_key, access_token_secret,
					client_args=client_args)
stream.statuses.filter(track='a')
#stream._request(url)
stream.site(follow='twitter')
