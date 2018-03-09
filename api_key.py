
import time

def obfuscateApiKey() :
    seed = 'jj7tg80fEGao'
    now = str(long(time.time() * 1000))
    n = now[-6:]
    r = str(int(n) >> 1).zfill(6)
    key = ""
    for i in range(0, len(n), 1):
      key += seed[int(n[i])]
    for j in range(0, len(r), 1):
      key += seed[int(r[j])+2]

    print "Timestamp:%s     Key:%s" % (now, key)
    return (now,key)
