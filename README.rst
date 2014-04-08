==================================
Django Trigger Happy : Service RSS
==================================

This service provides a way to get the RSS/ATOM Feeds that will be automatically
created in the service of your choice from Trigger Happy

Requirements :
==============
* django_th: 0.8.3
* feedparser: 5.1.3
* httplib2: 0.8
* PyTidylib : 0.2.1


Installation:
=============
to get the project, from your virtualenv, do :

.. code:: python

    pip install django-th-rss
    
then

.. code:: python

    python manage.py syncdb

to startup the database

Parameters :
============
As usual you will setup the database parameters.

Important parts are the settings of the available services :

Settings.py 
-----------

INSTALLED_APPS
~~~~~~~~~~~~~~

add the module th_rss to INSTALLED_APPS

.. code:: python

    INSTALLED_APPS = (
        'th_rss',
    )    

TH_SERVICES 
~~~~~~~~~~~

TH_SERVICES is a list of the services use by Trigger Happy

.. code:: python

    TH_SERVICES = (
        'th_rss.my_rss.ServiceRss',
    )


Setting up : Administration
===========================

once the module is installed, go to the admin panel and activate the service RSS. 

All you can decide here is to tell if the service requires an external authentication or not.

Once they are activated. User can use them.



