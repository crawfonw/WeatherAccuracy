#!/usr/bin/env python
import os

def purge_and_create_site_and_auth():
    #from django.contrib.sites.models import Site
    from django.conf import settings

#     Site.objects.all().delete()
# 
#     site = Site()
#     site.id = 1
#     site.domain = 'http://weather.presidentnick.com'
#     site.name = 'WeatherAccuracy'
#     site.save()

    from django.contrib.auth.models import Group, Permission, User
    
    User.objects.all().delete()
    
    user = User.objects.create_user('nick', 'fake@email.com')
    user.first_name = 'N'
    user.last_name = 'C'
    user.is_staff = True
    user.is_superuser = True
    user.set_password('a')
    user.save()

def run(purge):
    
    if purge:
        print 'Resetting site and auth data'
        purge_and_create_site_and_auth()
    
    from blog.models import BlogPost
    #BlogPost.objects.all().delete()
    #create_blogposts()
    
    from tracker.models import City, Query
    City.objects.all().delete()
    Query.objects.all().delete()
    create_cities()

def create_blogposts():
    from blog.models import BlogPost
    from django.contrib.auth.models import User
    import datetime
    
    user = User.objects.get(username='nick')
    now = datetime.datetime.now()
    BlogPost.objects.create(author=user, title='Test Post', post_date=now, is_draft=False, body='<p>This is a test post. Here is some HTML:</p><p><ol><li>One</li><li>Two</li></ol></p>')
    BlogPost.objects.create(author=user, title='Draft Post', post_date=now+datetime.timedelta(hours=6), is_draft=True, body='This should not show up on the front page.')

def create_cities():
    from tracker.models import City
    City.objects.create(name='Auckland, NZ', city_id=2193733)
    City.objects.create(name='Cairo, EG', city_id=360630)
    City.objects.create(name='Kyoto, JP', city_id=1857910)
    City.objects.create(name='Lima, PE', city_id=3936456)
    City.objects.create(name='London, England; UK', city_id=2643743)
    City.objects.create(name='Louisville, KY; USA', city_id=4299276)
    City.objects.create(name='San Francisco, CA; USA', city_id=5391959)
    City.objects.create(name='Ft. Myers Beach, FL; USA', city_id=4155996)
    City.objects.create(name='Boston, MA; USA', city_id=4930956)

if __name__ == '__main__':
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help='Reset site settings and auth system.')
    args = parser.parse_args()
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeatherAccuracy.settings")
    run(args.p)