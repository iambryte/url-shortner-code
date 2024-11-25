import pyshorteners
long_url = input ("enter the ur] to shorten")
type_tiny = pyshorteners.Shortener()
short_ur1 = type_tiny.tinyurl.short(long_url)
print("the shortened URL is:" + short_ur1)