from PyDigger import fetch

import os
import yaml

def test_vcs(tmpdir):
    print(tmpdir)
    config_file = os.environ['PYDIGGER_CONFIG'] = os.path.join(tmpdir, 'config.yml')
    print(os.environ['PYDIGGER_CONFIG'])
    config = {'github-token': 'fake'}
    with open(config_file, 'w') as outfile:
            yaml.dump(config, outfile, default_flow_style=False)

    package = fetch.PyPackage("foo")
    package.entry['home_page'] = 'https://github.com/user/project'
    package.entry['version'] = '1.0'
    package.extract_vcs()
    assert package.entry == {
        'home_page': 'https://github.com/user/project',
        'version': '1.0',
        'github': True,
        'gitlab': False,
        'bitbucket': False,
        'github_user': 'user',
        'github_project': 'project'
    }

    package = fetch.PyPackage("foo")
    package.entry['home_page'] = 'https://gitlab.com/user/project'
    package.entry['version'] = 'abc'
    package.extract_vcs()
    assert package.entry == {
        'home_page': 'https://gitlab.com/user/project',
        'version': 'abc',
        'github': False,
        'gitlab': True,
        'bitbucket': False,
        'gitlab_user': 'user',
        'gitlab_project': 'project'
    }

