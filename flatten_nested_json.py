
from typing import Any


class FlattenJson:
    
    result = {}
    
    def get_flat_json(self, js: Any):
        self.flat_json(js, '')
        return self.result
    
    def flat_json(self, js, name):
        
        if type(js) is dict:
            for key in js:
                self.flat_json(js[key], name + key + '_')
        elif type(js) is list:
            for index, value in enumerate(js):
                self.flat_json(value, name + str(index) + '_')
        else:
            self.result[name[:-1]]= js

if __name__ == '__main__':
    data = {'user' :
               {'Rachel':
                {'UserID':1717171717,
                'Email': 'rachel1999@gmail.com', 
                'friends': ['John', 'Jeremy', 'Emily']
                }
               }
              }
    obj = FlattenJson()
    print(obj.get_flat_json(data))