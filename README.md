# Jinja2 Modern

Jinja2 tags for modern web. Includes sass, scss, less, coffee, uglify. Can be easily extended for any command line tools.
Preprocessors not running if source files not changed.

## Instalation

```shell
pip install jinja2modern
```

## Usage

In your project directory create settings.py, guess you already have it, with settings:

### Basic settings:

```python
#home path
JINJA2MODERN_HOME = os.path.realpath(os.path.dirname(__file__))
#media path relative to home directory
JINJA2MODERN_MEDIA_PATH = 'media'
#media url
JINJA2MODERN_MEDIA_URL = '/media'
```

#### Engines

There are several preprocessor engines that you will need in your project. Here is how you can get them:

```python
JINJA2MODERN_ENGINES = {
    'coffee': '/path/to/coffee/bin/coffee',
    'uglify': '/path/to/uglify/bin/uglifyjs',
    'lesscss': '/path/to/lesscss/bin/lessc',
    'sass': '/path/to/sass/bin/sass',
}
```

### Templates

You always can overide basic templates by placing it in tags subdirectory in your jinja2 environment template directory

#### js.html:

```jinja
<script src="{{ file_link }}"></script>
```

#### css.html:

```jinja
<link rel="stylesheet" type="text/css" href="{{ file_link }}" />
```

## Tags

### Less, Sass, Scss

All of this template code:

```jinja
{% less "style.css" %}
    less/style.less
{% endless %}
```

```jinja
{% less "less/style.less" %}
```

will render tags/css.html, for default template:
`<link rel="stylesheet" type="text/css" href="/media_url/css/style.css" />`

Of course you can specify out path and file name

```jinja
{% less "path/to/style.css" %}
    less/style.less
{% endless %}
```

this will render tags/css.html, for default template:
`<link rel="stylesheet" type="text/css" href="/media_url/path/to/style.css" />`


### Javascript

Js tag just copy files to media path

```jinja
{% js "js/main/main.js" %}
```

this will render tags/js.html, for default template:
`<script src="/media_url/js/main.js"></script>`

#### Advanced js tag using:

You can specify librarys for using in your templates by set this in your settings.py

```python
JINJA2MODERN_JS_LIBS_PATH = 'js/libs'
JINJA2MODERN_JS_LIBS = {
    'jquery': {
        'src': 'js/lib/jquery*.js',
        'template': 'js/jquery.html'
    },
}
```

and then just use

```jinja
{% js "jquery" %}
```

this will render template js/jquery.html

```jinja
<script src="//ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="{{ file_link }}"><\/script>')</script>
```


### Coffee script

All of this template code:

```jinja
{% coffee "js/main/main.coffee" %}
```

```jinja
{% coffee "main.js" %}
    js/main/main.coffee
{% endcoffee %}
```

```jinja
{% coffee "main.js" %}
    js/main/main1.coffee
    js/main/main2.coffee
    js/main/main3.coffee
{% endcoffee %}
```

will render tags/js.html, for default template:
`<script src="/media/url/js/main.js"></script>`

and of course you can specify out path and file name like for less tag.

### UglifyJS

All of this template code:

```jinja
{% uglify "js/main/main.js" %}
```

```jinja
{% uglify "main.js" %}
    js/main/main.js
{% enduglify %}
```

```jinja
{% uglify "main.js" %}
    js/main/main1.js
    js/main/main2.js
    js/main/main3.js
{% enduglify %}
```

will render tags/js.html, for default template:
`<script src="/media/url/js/main.js"></script>`

### Advanced coffee and uglify tag using:

__In this case uglify will run on every template rendering__

```jinja
{% coffee "main.js" %}
    js/main/main1.coffee
    js/main/main2.coffee
    js/main/main3.coffee
{% endcoffee %}
{% uglify %}
    /media/url/js/main.js
{% enduglify %}
```

Coffee tag will produce `/media/url/js/main.js` and render tags/js.html template. Than uglify will compress this file and will not render any templates.

## Roadmap ##

- Rewrite to optionally use python packages to compile instead of executables
- Publish to Pypi
- Integrate with Flask instead of just Jinja2
- Once integration is done, rename to flask_j2modern
- Set it and forget it feature (master template command)

## Credit ##

>Forked from version 0.3.0 of Jinja2Modern.
>
>Authored by Alexey Novikov <velocityzen@gmail.com>
>
>https://github.com/velocityzen/jinja2modern
