f = open('db.txt', 'a')


def add_to_db(data: int):
    f.write(str(data))
    f.write('\n')
