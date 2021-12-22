import json
from copy import copy
from enum import Enum
from functools import reduce
from os.path import isdir
from re import match, sub, search
from sys import argv


class Digits(str, Enum):
    M = 'major'
    m = 'minor'
    p = 'patch'


class VersionLocker:
    """
    Class locks versions of packages in Pipfile accordingly with certain versions from Pipfile.lock.
    Requirements:
        1) Have Pipfile, Pipfile.lock in root of project.
    How to use:
        1) Give absolute path of project root to VersionLocker constructor.
        2) To apply versions locking call public method lock_versions().

    Класс фиксирует версии пакетов в Pipfile в соответствии с данными в Pipfile.lock.
    Требуется:
        1) В корне проекта должны быть валидные Pipfile и Pipfile.lock файлы.
    Как использовать:
        1) В конструктор передаётся абсолютный путь к корню проекта.
        2) Для обновления Pipfile вызывается единственный публичный метод lock_versions().
    """

    def __init__(self, root_path: str, only_unlocked: bool = True, digit: Digits = Digits.M):
        """
        :param root_path: absolute path to python project's root
        :param only_unlocked: if it's True then it changes only unlocked packaged.
        In other words, <package> = "*".
        :param digit: It means what a version digit the util must lock to, inclusively.
        """

        self.re_for_package_checking_on_lock = r'\"(?:(?:(?:==|<=?)\d+(?:.(?:\d+|\*)){0,2}))\"' if only_unlocked \
            else r'\"==\d+.\*\"'
        self.re_for_version_getting, self.version_suffix = self.get_re_for_version_getting_and_version_suffix(digit)
        self.lines = None
        self.packages = []
        self.packages_lines = {}
        self.path = root_path if root_path[-1] == '/' else root_path + '/'
        self.packages_versions = None

        self._get_pipfile_packages()
        self._get_versions()

    @staticmethod
    def get_re_for_version_getting_and_version_suffix(digit: Digits):
        return {
            Digits.M: (r'(?P<version>==\d+.)', '*"'),
            Digits.m: (r'(?P<version>==(?:\d+.){2})', '*"'),
            Digits.p: (r'(?P<version>==(?:\d+.){2}\d+)', '"')
        }[digit]

    def _get_pipfile_packages(self):
        with open(self.path + 'Pipfile', 'r') as file:
            self.lines = file.readlines()
            is_package_line = False
            for ind, line in enumerate(self.lines):
                if line.startswith('[dev-packages]') or line.startswith('[packages]'):
                    is_package_line = True
                elif is_package_line:
                    if group := match(r'\"?(?P<package>\w+(?:[-_]\w+)*)\"?\s*=\s*', line):
                        is_already_locked = search(self.re_for_package_checking_on_lock, line)
                        if is_already_locked:
                            continue
                        package = group['package'].lower().replace('_', '-')
                        self.packages.append(package)
                        self.packages_lines[package] = ind
                    else:
                        is_package_line = False

    def _get_versions(self):
        with open(self.path + 'Pipfile.lock', 'r') as file:
            pipfile_lock = json.load(file)
        versions = reduce(lambda d, x: {**d, **{x[0]: x[1]['version']}},
                          tuple(pipfile_lock['default'].items()) + tuple(pipfile_lock['develop'].items()),
                          {})
        self.packages_versions = {package: '"' + match(self.re_for_version_getting, versions[package])['version'] +
                                           self.version_suffix
                                  for package in self.packages if package in versions}

    def lock_versions(self):
        absent_in_pipfile_lock_packages = []
        unsuccessful_locking = []
        lines = copy(self.lines)
        for package in self.packages:
            version = self.packages_versions.get(package, None)

            if not version:
                absent_in_pipfile_lock_packages.append(package)
                continue

            line_ind = self.packages_lines[package]
            line = lines[line_ind]
            new_line = sub(r'\"(?:(?:(?:==|<=?)\d+(?:.(?:\d+|\*)){0,2})|\*)\"', version, line)
            if line == new_line:
                unsuccessful_locking.append(package)
            else:
                lines[line_ind] = new_line
        with open(self.path + 'Pipfile', 'w') as file:
            for line in lines:
                file.write(line)
            if len(absent_in_pipfile_lock_packages):
                file.write('\nabsent in pipfile lock packages:\n')
                for package in absent_in_pipfile_lock_packages:
                    file.write(package+'\n')
            if len(unsuccessful_locking):
                file.write('\nunsuccessful locking:\n')
                for package in unsuccessful_locking:
                    file.write(package+'\n')


if __name__ == '__main__':
    assert len(argv) == 4, f'Pass 3 args: root_path, is_only_unlocked, digit'
    _, root_path, is_only_unlocked, digit = argv
    assert isdir(root_path), 'String should be abs path of project root!/' \
                             'Строка должна быть абсолютным путём к корню проекта!'
    assert is_only_unlocked in ['y', 'n'], 'String should be one of "y"/"n" value.'
    assert digit in tuple(map(lambda d: d.value, Digits)), 'String should be one of "major"/"minor"/"patch" value.'
    is_only_unlocked = {'y': True, 'n': False}[is_only_unlocked]
    version_locker_obj = VersionLocker(root_path, only_unlocked=is_only_unlocked, digit=digit)
    version_locker_obj.lock_versions()
