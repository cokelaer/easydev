"""Test make_develop for Multisetup object"""
import os
from easydev.multisetup import Multisetup
from nose import with_setup

"""!!For the following test, don't use intrusive commands such as install 
together with run method. !!!!"""

curdir = '..' + os.sep + '..'

packages = ['easydev']
def test_init():
    """ Test initialization of Multisetup object """
    mysetup = Multisetup(curdir=curdir, commands='build', packages=packages)
    assert mysetup.commands == ['build']
    assert len(mysetup.packages) == 1
    assert mysetup.packages == packages


def _test_wrong_package():
    mysetup = Multisetup(curdir=curdir, 
                         commands=['build', '--packages','corezzz'],
                         packages=['corezzz'])
    try:
        mysetup.run()
        assert False
    except:
        assert True


def test_parse_packages():
    """ Test of parse_packages() method with option --packages"""
    mysetup = Multisetup(curdir=curdir, commands='dummy', packages=packages)
    mysetup.commands = ['build', '--packages', 'easydev']
    mysetup.parse_packages()
    assert mysetup.packages ==  set(['easydev'])


def test_parse_no_packages():
    """ Test of parse_packages() method with option --exclude-package"""

    mysetup = Multisetup(curdir=curdir, 
                         commands='commands --exclude-packages easydev', 
                         packages=packages)

    print(mysetup.packages)
    assert mysetup.packages == []


def test_parse_commands():
    """ Test of parse_commands() method"""
    commands =['install', 'sdist', '-d', './dist', '--quiet', '--keep-going']
    mysetup = Multisetup(curdir=curdir, commands=commands, packages=[])


    mysetup.parse_commands()
    mysetup.parse_packages()


    assert len(mysetup.commands) == 2
    assert mysetup.commands[0] == 'install'
    assert mysetup.commands[1] == 'sdist -d ./dist'
    assert mysetup.verbose == False
    assert mysetup.force == True 


def test_setup_failure():
    """ Test of run() method with bad option"""
    commands = '--packages easydev sdist --bad-option'
    mysetup = Multisetup(curdir=curdir, commands=commands, packages=['easydev'])

    try:
        mysetup.run()
        assert False
    except:
        assert True







