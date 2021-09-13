

class KwargsTest:
    
    def test_kw(self, ar, **kwargs):
        salt_logs = {'optional_service_params':  {'include-salt-logs': ''}}
        print(ar, {**kwargs, **salt_logs})
    

if __name__ == '__main__':
    obj = KwargsTest()
    obj.test_kw(12, optional_service_params={'excluede': ''})