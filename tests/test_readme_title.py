import os


def test_readme_title():
    here = os.path.dirname(__file__)
    readme_path = os.path.abspath(os.path.join(here, '..', 'README.md'))
    with open(readme_path, encoding='utf-8') as f:
        first_line = f.readline().rstrip('\n')
    assert first_line == '# empty_project_readme', "README title should be '# empty_project_readme'"
