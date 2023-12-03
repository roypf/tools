class Logger:
    def __init__(self, filename):
        self.data = {}
        self.filename = filename
        open(self.filename, 'a').close()
        self.read()


    def read(self):
        data = []
        with open(self.filename, 'r') as file:
            for row in file:
                data.append(row.strip().split(';'))
        for row in data:
            self.data.update({row[0]: (row[1:])})


    def write(self):
        with open(self.filename, 'w') as file:
            for key, value in self.data.items():
                file.write(f'{key};{";".join(value)}\n')


    def update(self, key, value):
        if key in self.data:
            if value not in self.data[key]:
                self.data[key].append(value)
                self.write()
            else:
                return
        else:
            self.data.update({key: [value]})
            self.write()
        #print(key, 'update:', value)


if __name__ == '__main__':
    log = Logger('log_example.csv')
    log.update('log', 'data')
    if 'data' in log.data['log']:
        for key, value in log.data.items():
            print(f'{key} - {" ".join(value)}')
