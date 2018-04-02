# Py-sms-api with eve

[![Build Status](https://travis-ci.org/frodonLD/eve-rest-api.svg?branch=master)](https://travis-ci.org/frodonLD/eve-rest-api)

* python as language
* [eve](http://python-eve.org/config.html) as framework
* mongodb as database
* [Distutils Python Setup script](https://docs.python.org/3.6/distutils/setupscript.html) as module distribution 

## Setup 
Setup is handled by [Distutils](https://docs.python.org/3.6/distutils/setupscript.html) just by writing the [setup file](setup.py)

## Eve config file 

This is the most important part of the app. In this file named `settings.py` you configure your whole app by setting your domain and the different restrictions to your rest api and also the dtabase you want to use. 
This file should be at the root of your project. check [http://python-eve.org/config.html](http://python-eve.org/config.html) to know more about the config file.

## How does it work 

Eve is designed to do basics CRUD operations for you. It is based on [flask](http://flask.pocoo.org/) which is an awesome framework to build rest api in python. 
So ou have nothing to do except define your domain and restriction in the [config file](settings.py). 
All basics CRUD operations will be handled (depends on which restrictions you configure). Your app is up and you can enjoy your api.

## Everything is event with eve

You can imagine more complex operations with eve. You can set up some hooks to fire. 
For example you can execute some code **before** *all inserts* or just before a *particular resource insert*. 
The hooks are evailable for a lot of events. You can check [eve events hooks](http://python-eve.org/features.html#eventhooks) for more examples. [Discover features of eve](http://python-eve.org/features.html).

## Launch the app

```bash
docker-compose up -d
```

You can try post on `localhost:${PORT}/sms` with these differents body below:

**Will fail due to missing/empty required field `from`**

```json
{
	"to": "you",
	"content": "a text message from me to you",
	"incoming": true,
	"hash": "some-hash",
	"sms_date": "2018-04-02 17:56:03"
}
```

**Will fail due to incorrect datefield `sms_date`**
```json
{
    "from": "me",
	"to": "you",
	"content": "a text message from me to you",
	"incoming": true,
	"hash": "some-hash",
	"sms_date": "fake date"
}
```

**Will succeed `sms_date`**
```json
{
    "from": "me",
	"to": "you",
	"content": "a text message from me to you",
	"incoming": true,
	"hash": "some-hash",
	"sms_date": "2018-04-02 17:56:03"
}
```