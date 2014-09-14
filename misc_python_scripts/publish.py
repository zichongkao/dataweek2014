from Pubnub import Pubnub
import time

publish_key = 'pub-c-f044f713-537b-46b2-b775-ba30f4a4c0a9'
subscribe_key = 'sub-c-df50be56-35f4-11e4-8736-02ee2ddab7fe'
secret_key = 'sec-c-MjFjYmEzOTYtYTk5ZS00ZDRjLTkzMzMtODBlNGRmYjI5N2Nk'
cipher_key = ''
ssl_on = False

pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'countChannel'

countlist = [46, 48, 51, 51, 49, 49, 50, 50, 50, 51, 51, 51, 50, 50, 53, 53, 53,
       47, 55, 56, 56, 56, 55, 55, 53, 54, 54, 54, 52, 59, 62, 61, 61, 61,
       60, 60, 59, 65, 61, 65, 63, 63, 59, 59, 59, 59, 58, 59, 58, 60, 59,
       58, 60, 60, 62, 59, 61, 62, 61, 63, 61, 61, 64, 64, 63, 63, 62, 65,
       59, 59, 59, 60, 60, 60, 61, 61, 61, 64, 66, 63, 63, 63, 67, 67, 67,
       65, 67, 71, 70, 68, 68, 70, 70, 70, 72, 72, 73, 73, 77, 76, 78, 78,
       75, 75, 78, 78, 79, 79, 78, 78, 79, 79, 79, 80, 78, 81, 77, 80, 76,
       81, 78, 79, 83, 83, 80, 80, 80, 80, 81, 75, 75, 76, 74, 77, 75, 79,
       79, 82, 81, 79, 80, 80, 80, 80, 80, 83, 81, 84, 83, 80, 80, 82, 78,
       77, 80, 80, 85, 84, 83, 86, 82, 82, 86, 86, 83, 83, 83, 82, 83, 79,
       80, 80, 80, 80, 79, 73, 80, 81, 79, 74, 78, 80, 76, 75, 71, 71, 73,
       71, 72, 73, 73, 73, 75, 75, 76, 76, 74, 70, 71, 69, 69, 70, 72, 72,
       74, 72, 72, 73, 73, 71, 69, 69, 70, 69, 69, 69, 68, 68, 68, 69, 72,
       72, 73, 72, 72, 72, 73, 73, 70, 70, 71, 71, 71, 71, 71, 72, 74, 74,
       78, 77, 78, 79, 82, 82, 74, 74, 74, 73, 73, 73, 76, 76, 77, 77, 77,
       77, 77, 74, 85, 85, 86, 85, 85, 85, 85, 86, 86, 87, 85, 85, 86, 85,
       85, 91, 89, 89, 91, 91, 90, 89, 89, 88, 87, 87, 89, 89, 90, 86, 86,
       86, 86, 86, 85, 85, 79, 82, 81, 81, 83, 81, 78, 79, 82, 82, 83, 83,
       84, 84, 83, 83, 81, 81, 79, 79, 78, 78, 78, 78, 79, 79, 81, 81, 79,
       79, 79, 79, 79, 76, 77, 79, 77, 77, 77, 76, 78, 78, 78, 78, 82, 83,
       84, 81, 81, 81, 80, 80, 78, 75, 78, 78, 78, 78, 76, 77, 77, 82, 81,
       80, 80, 80, 80, 75, 76, 76, 76, 77, 78, 78, 78, 76, 76, 76, 78, 77,
       77, 74, 75, 75, 75, 75, 75, 73, 75, 75, 75, 74, 76, 76, 73, 73, 78,
       78, 79, 80, 79, 79, 79, 78, 77, 77, 77, 77, 79, 79, 76, 75, 76, 79,
       76, 76, 76, 76, 78, 78, 78, 79, 79, 82, 82, 76, 76, 76, 75, 75, 73,
       73, 73, 73, 73, 73, 73, 70, 71, 71, 74, 74, 76, 75, 73, 72, 71, 71,
       73, 72, 71, 72, 72, 72, 72, 76, 77, 77, 77, 77, 81, 81, 81, 84, 84,
       84, 84, 81, 81, 81, 77, 77, 77, 81, 80, 82, 82, 79, 83, 83, 80, 76,
       76, 77, 78, 77, 80, 80, 81, 81, 85, 85, 83, 78, 77, 77, 79, 79, 80,
       79, 81, 81, 81, 81, 78, 78, 79, 80, 78, 78, 75, 72, 72, 74, 74, 75,
       74, 74, 74, 81, 79, 78, 79, 81, 81, 83, 82, 80, 80, 80, 80, 88, 87,
       86, 85, 86, 86, 83, 83, 84, 83, 79, 79, 79, 80, 80, 80, 81, 79, 79,
       81, 81, 82, 78, 79, 74, 74, 79, 80, 80, 81, 81, 81, 85, 83, 60, 60, 
       62, 59, 61, 62, 61, 63, 61, 61, 64, 64, 63, 63, 62, 65,
       59, 59, 59, 60, 60, 60, 61, 61, 61, 64, 66, 63, 63, 63, 67, 67, 67,
       65, 67, 71, 70, 68, 68, 70, 70, 70, 72, 72, 73, 73, 77, 76, 78, 78,
       75, 75, 78, 78, 79, 79, 78, 78, 79, 79, 79, 80, 78, 81, 77, 80, 76,
       81, 78, 79, 83, 83, 80, 80, 80, 80, 81, 75, 75, 76, 74, 77, 75, 79,
       79, 82, 81, 79, 80, 80, 80, 80, 80, 83, 81, 84, 83, 80, 80, 82, 78,
       77, 80, 80, 85, 84, 83, 86, 82, 82, 86, 86, 83, 83, 83, 82, 83, 79,
       80, 80, 80, 80, 79, 73, 80, 81, 79, 74, 78, 80, 76, 75, 71, 71, 73,
       71, 72, 73, 73, 73, 75, 75, 76, 76, 74, 70, 71, 69, 69, 70, 72, 72,
       74, 72, 72, 73, 73, 71, 69, 69, 70, 69, 69, 69, 68, 68, 68, 69, 72,
       72, 73, 72, 72, 72, 73, 73, 70, 70, 71, 71, 71, 71, 71, 72, 74, 74,
       78, 77, 78, 79, 82, 82, 74, 74, 74, 73, 73, 73, 76, 76, 77, 77, 77,
       77, 77, 74, 85, 85, 86, 85, 85, 85, 85, 86, 86, 87, 85, 85, 86, 85,
       85, 91, 89, 89, 91, 91, 90, 89, 89, 88, 87, 87, 89, 89, 90, 86, 86,
       86, 86, 86, 85, 85, 79, 82, 81, 81, 83, 81, 78, 79, 82, 82, 83, 83,
       84, 84, 83, 83, 81, 81, 79, 79, 78, 78, 78, 78, 79, 79, 81, 81, 79,
       79, 79, 79, 79, 76, 77, 79, 77, 77, 77, 76, 78, 78, 78, 78, 82, 83,
       84, 81, 81, 81, 80, 80, 78, 75, 78, 78, 78, 78, 76, 77, 77, 82, 81,
       80, 80, 80, 80, 75, 76, 76, 76, 77, 78, 78, 78, 76, 76, 76, 78, 77,
       77, 74, 75, 75, 75, 75, 75, 73, 75, 75, 75, 74, 76, 76, 73, 73, 78,
       78, 79, 80, 79, 79, 79, 78, 77, 77, 77, 77, 79, 79, 76, 75, 76, 79,
       76, 76, 76, 76, 78, 78, 78, 79, 79, 82, 82, 76, 76, 76, 75, 75, 73,
       73, 73, 73, 73, 73, 73, 70, 71, 71, 74, 74, 76, 75, 73, 72, 71, 71,
       73, 72, 71, 72, 72, 72, 72, 76, 77, 77, 77, 77, 81, 81, 81, 84, 84,
       84, 84, 81, 81, 81, 77, 77, 77, 81, 80, 82, 82, 79, 83, 83, 80, 76,
       76, 77, 78, 77, 80, 80, 81, 81, 85, 85, 83, 78, 77, 77, 79, 79, 80,
       79, 81, 81, 81, 81, 78, 78, 79, 80, 78, 78, 75, 72, 72, 74, 74, 75,
       74, 74, 74, 81, 79, 78, 79, 81, 81, 83, 82, 80, 80, 80, 80, 88, 87,
       86, 85, 86, 86, 83, 83, 84, 83, 79, 79, 79, 80, 80, 80, 81, 79, 79,
       81, 81, 82, 78, 79, 74, 74, 79, 80, 80, 81, 81, 81, 85, 83]

while True:
	for count in countlist:
		pubnub.publish(channel, count)
		time.sleep(0.3)





