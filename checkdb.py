import sqlite3

db = sqlite3.connect("account.sqlite", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

for row in db.execute("SELECT * FROM localhistory"):
    local_time = row[0]
    print("{}\t{}".format(local_time, type(local_time)))
# Changes here2
db.close()
