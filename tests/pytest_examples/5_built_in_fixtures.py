import os.path


def test_use_capsys(capsys):
    """capsys built in fixture"""
    print('hello')

    captured = capsys.readouterr()

    assert captured.out == "hello\n"


def test_create_file(tmpdir):
    """tmpdir built in fixture

    pytest --basetemp=here/ 5_built_in_fixtures.py

    """
    p = tmpdir.mkdir('temp_dir').join('temp_file.txt')
    p.write('content')
    assert p.read() == 'content'
    assert len(tmpdir.listdir()) == 1


def getssh(username):
    return os.path.join(os.path.expanduser(f'~{username}'), '.ssh')


def test_path_to_ssh_config_for_username(monkeypatch):
    def mock_return(path):
        return '/home/root/'

    monkeypatch.setattr(os.path, 'expanduser', mock_return)

    assert getssh('root') == '/home/root/.ssh'
