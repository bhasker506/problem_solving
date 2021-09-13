import json

def get_latest_values():
    data = {}
    with open('/Users/greddy/Documents/workspace/cdpmc-qe/v3-test-freeipa-image-catalog.json', 'r') as r:
        data = json.load(r)
    
    freeipa_images = data['images']['freeipa-images']
    freeipa_images = sorted(freeipa_images, key=lambda i: i['created'], reverse=True)
    print(freeipa_images)

get_latest_values()