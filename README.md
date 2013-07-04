Django Trigger Happy : Service RSS
==================================

This service provide a way to get the RSS/ATOM Feeds that will be automatically created in the service of your choice

Requirements :
-------------
* django_th 0.4.0
* feedparser 5.1.3
* httplib2 0.8
* ordereddict 1.1
* PyTidylib : 0.2.1

Installation:
------------
to get the project, from your virtualenv, do :
```system
pip install django-th-rss
```
then
```python
python manage.py syncdb
```
to startup the database

Parameters :
------------
As usual you will setup the database parameters.

Important parts are the settings of the available services :

### Settings.py 

#### INSTALLED_APPS

add the module th_rss to INSTALLED_APPS

#### TH_SERVICES 

TH_SERVICES is a list of the services we put in django_th/services directory

```python
TH_SERVICES = (
    'th_rss.my_rss.ServiceRss',
)
```

#### Wizard Template TH_WIZARD_TPL
```python
TH_WIZARD_TPL = {
    'my_rss':
    'my_rss/rss-form.html',
}
```



Setting up : Administration
---------------------------

once the module is installed, go to the admin panel and activate the service RSS. 

All you can decide here is to tell if the service requires an external authentication or not.

Once they are activated. User can use them.



