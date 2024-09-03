from threading import Thread

def argsReader(a1, a2):
    print(a1)
    print(a2)

print('Hello!')
s = 'Hello!'

t1 = Thread(target=print, args='Hello!')
t2 = Thread(target=print, args=s)

t1.start()
t2.start()

t1.join()
t2.join()

t = []
for i in range(4):
    t.append(Thread(target=argsReader, args=('h', 'l')))
    t[i].start()

for i in range(4):
    t[i].join()
