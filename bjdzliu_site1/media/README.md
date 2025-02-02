### static
#### STATIC_URL = 'static/'
default
http://127.0.0.1:8000/static/1.jpg

add extra dir
```
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'helloWorld/static',
    BASE_DIR / 'helloworld/images',
]
```


### media
http://127.0.0.1:8000/media/media_1.jpg

