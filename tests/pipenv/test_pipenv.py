from unittest.mock import mock_open, patch
from pipenv.version_locker_utils import VersionLocker, Digits
from tests.pipenv.data import (
    test_pipfile, pipfile, pipfile_lock, test_pipfile_only_unlocked, test_pipfile_minor,
    test_pipfile_only_unlocked_and_minor, test_pipfile_fix, test_pipfile_only_unlocked_and_fix
)


class File:
    def __init__(self):
        self.result = ''

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def write(self, line):
        self.result += line


def _test_version_locker(test_pipfile, only_unlocked, digit):
    root_path = '/'
    open_name = 'rti_dev_utils.pipenv.version_locker_utils.open'
    with patch(open_name, mock_open(read_data=pipfile)) as file:
        result_file = File()
        files = (file.return_value, mock_open(read_data=pipfile_lock).return_value, result_file)
        file.side_effect = files
        version_locker_obj = VersionLocker(root_path, only_unlocked=only_unlocked, digit=digit)
        version_locker_obj.lock_versions()
        for result, test in zip(result_file.result.split('\n'), test_pipfile.split('\n')):
            assert result == test


def test_version_locker_not_only_unlocked_and_major():
    _test_version_locker(test_pipfile, False, Digits.M)


def test_version_locker_only_unlocked_and_major():
    _test_version_locker(test_pipfile_only_unlocked, True, Digits.M)


def test_version_locker_not_only_unlocked_and_minor():
    _test_version_locker(test_pipfile_minor, False, Digits.m)


def test_version_locker_only_unlocked_and_minor():
    _test_version_locker(test_pipfile_only_unlocked_and_minor, True, Digits.m)


def test_version_locker_not_only_unlocked_and_fix():
    _test_version_locker(test_pipfile_fix, False, Digits.p)


def test_version_locker_only_unlocked_and_fix():
    _test_version_locker(test_pipfile_only_unlocked_and_fix, True, Digits.p)
