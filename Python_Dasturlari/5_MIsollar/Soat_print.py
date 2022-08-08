from time import gmtime, strftime

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%a, %Y %H:%M:%S +0000", gmtime()))
print(strftime("%d, %Y %H:%M:%S +0000", gmtime()))
print(strftime("%b, %Y %H:%M:%S +0000", gmtime()))
print(strftime("%Y %H:%M:%S +0000", gmtime()))
print(strftime("%H:%M:%S +0000", gmtime()))
print(strftime("%M:%S +0000", gmtime()))
print(strftime("%S +0000", gmtime()))
print(strftime("0000", gmtime()))
