import common.validators2 as validators
import common

#import common.models.posts
#import common.models.posts.posts
#import common.models.users
import common.models as models
#from common.models import *
import  common.helpers as helpers

validators.boolean.is_boolean('true')
validators.json.is_json('{}')
validators.is_numeric(10)
validators.is_date('2020-0224')


john_post = models.Post()
john_post = models.Posts()
john = models.User()

print('\n\n****** self ******')
for k in dict(globals()).keys():
    print(k)

print('\n\n****** common ******')
for k in common.__dict__.keys():
    print(k)

print('\n\n****** models ******')
for k in common.models.__dict__.keys():
    print(k)


print(helpers.say_hello('Python'))
print(helpers.factorial(5))

import asyncio
import email