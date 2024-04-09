from girls_day import GDMessageHandler

mh = GDMessageHandler()
mh.q.put(True)
mh.q.put(False)