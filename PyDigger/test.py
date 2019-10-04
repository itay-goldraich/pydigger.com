import PyDigger.common
import os
import sys
import yaml

root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root)


class TestDigger(object):
    def test_fix(self):
        assert 1 == 1

    def test_common(self):
        root = PyDigger.common.get_root()
        source_dir = PyDigger.common.get_source_dir()
        assert root + '/src' == source_dir

# TODO: Make sure the web site can be loaded even if the configuration files are missing and there is no access to the
# databse. Report this properly in the log or on the generate web page.

class TestWeb(object):
    def setup_class(self):
        create_config_files()
        import PyDigger.website
        self.app = PyDigger.website.app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        #print(rv.data)
        assert b'<title>PyDigger - unearthing stuff about Python</title>' in rv.data

    def test_stats(self):
        rv = self.app.get('/stats')
        assert rv.status == '200 OK'
        #print(rv.data)
        assert b'<title>PyDigger - Statistics</title>' in rv.data


    def test_about(self):
        rv = self.app.get('/about')
        assert rv.status == '200 OK'
        #print(rv.data)
        assert b'<title>About PyDigger</title>' in rv.data

def create_config_files():
    config_file = os.path.join(root, 'config.yml')
    if not os.path.exists(config_file):
        config = {
            "username": "",
            "password": "",
            "server": "localhost:27017"
        }
        with open(config_file, 'w') as outfile:
            yaml.dump(config, outfile, default_flow_style=False)

