try:
	from settings import JINJA2MODERN_JS_LIBS
except ImportError:
	JINJA2MODERN_JS_LIBS = {
		
	}

try:
	from settings import JINJA2MODERN_JS_LIBS_PATH
except ImportError:
	JINJA2MODERN_JS_LIBS_PATH = './js/libs/'

try:
	from settings import JINJA2MODERN_HOME
except ImportError:
	JINJA2MODERN_HOME = os.path.realpath(os.path.dirname(__file__))

try:
	from settings import JINJA2MODERN_MEDIA_PATH
except ImportError:
	JINJA2MODERN_MEDIA_PATH = 'public'

try:
	from settings import JINJA2MODERN_MEDIA_URL
except ImportError:
	JINJA2MODERN_MEDIA_URL = '/public'

try:
	from settings import JINJA2MODERN_ENGINES
except ImportError:
	JINJA2MODERN_ENGINES = {
		'coffee': '',
		'uglify': '',
		'lesscss': '',
		'sass': '',
	}
