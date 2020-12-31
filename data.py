import json
import os
import time


class DataStore:
    def __init__(self, file_name='data.json'):
        self.file_name = file_name
        if os.path.exists(file_name):
            with open(file_name) as file:
                if len(file.read()) > 0:
                    self.len = 1
                else:
                    self.len = 0
        else:
            with open(file_name, 'w'):
                pass
            self.len = 0

    def read(self, key):
        try:
            with open(self.file_name) as file:
                data = json.load(file)
            if data[key][1] == 0:
                return print(data[key][0])
            else:
                if time.time() < data[key][1]:
                    return print(data[key][0])
                else:
                    data.pop(key)
                    with open(self.file_name, 'w') as file:
                        json.dump(data, file)

        except KeyError as e:
            print('Key not found:', e)
        except Exception as e:
            print('unable to open file ', e)

    def create(self, key, value, timeout=0):
        try:
            with open(self.file_name) as file:
                if self.len == 1:
                    data = json.load(file)
                else:
                    data = dict()
            if key in data.keys():
                print('Key already exist')
            else:
                if timeout == 0:
                    data[key] = [value,0]
                else:
                    data[key] = [value, timeout + time.time()]
                with open(self.file_name, 'w+') as file:
                    json.dump(data, file)
                    print('created')
        except Exception as e:
            print('unable to open file ', e)

    def delete(self, key):
        try:
            with open(self.file_name) as file:
                data = json.load(file)
            data.pop(key)
            print('deleted')
            with open(self.file_name, 'w') as file:
                json.dump(data, file)

        except KeyError as e:
            print('Key not found:', e)
        except Exception as e:
            print('unable to open file ', e)
