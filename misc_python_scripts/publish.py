from Pubnub import Pubnub

publish_key = 'pub-c-f044f713-537b-46b2-b775-ba30f4a4c0a9'
subscribe_key = 'sub-c-df50be56-35f4-11e4-8736-02ee2ddab7fe'
secret_key = 'sec-c-MjFjYmEzOTYtYTk5ZS00ZDRjLTkzMzMtODBlNGRmYjI5N2Nk'
cipher_key = ''
ssl_on = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'countChannel'

while(True):
	pubnub.publish(channel, "100")