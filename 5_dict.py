

samsung = {'model':'a7',
        'display_width':1980,
        'display_heith':1080,
        'is_gprs':'Yes',
        'is_wi-fi':'Yes'
        }
iphone = {
        'model':7,
        'display_width':2200,
        'display_heith':1080,
        'is_gprs':'Yes',
        'is_wi-fi':'Yes'
         }
xiaomy = {
        'model':8,
        'display_width':2200,
        'display_heith':1080,
        'is_gprs':'Yes',
        'is_wi-fi':'Yes'
        }
nokia = {
        'model':6.01,
        'display_width':1800,
        'display_heith':900,
        'is_gprs':'Yes',
        'is_wi-fi':'Yes'
        }
print(samsung.items())



for i in samsung:
    #if 'display_width' > 2000 and 'display_heith' >= 1000:
        print(i['display_width'])


