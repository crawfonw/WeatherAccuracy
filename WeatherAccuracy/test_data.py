#!/usr/bin/env python
import os

def purge_and_create_site_and_auth():
    from django.contrib.sites.models import Site
    from django.conf import settings

    Site.objects.all().delete()

    site = Site()
    site.id = 1
    site.domain = 'http://www.rose-hulman.edu'
    site.name = 'WeatherAccuracy'
    site.save()

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
    
    from tracker.models import *
    City.objects.all().delete()
    Query.objects.all().delete()
    
    create_cities()
    
def create_cities():
    from tracker.models import City
    City.objects.create(name='London, England; UK', query_string='london,uk')
    City.objects.create(name='Louisville, KY; USA', query_string='louisville,ky')

if __name__ == '__main__':
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help='Reset site settings and auth system.')
    args = parser.parse_args()
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeatherAccuracy.settings")
    run(args.p)