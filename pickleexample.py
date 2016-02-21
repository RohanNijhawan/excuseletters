import pickle

f = open('pickletest.p', 'rb')
a = pickle.load(f)
f.close()

def add(key, value):
	a[key] = value
	print(value + " saved under " + key)

def save():
	f = open('pickletest.p', 'wb')
	pickle.dump(a, f)
	f.close()
	print("saved")