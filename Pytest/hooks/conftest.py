import pytest


def pytest_runtest_setup(item):
    print('Setup',item)


def pytest_cmdline_main(config):
    print(config.option)
    print(config.getoption('debug'))
    print(config.getoption('showcapture'))
    print(config.getoption('plugins'))



def pytest_cmdline_main(config):
    print("***pytest_cmdline_main ***", config)


def pytest_configure(config):
    print("*** pytest_configure ***", config)


def pytest_sessionstart(session):
    print('*** pytest_sessionstart ***', session)


def pytest_collection_modifyitems(session, config, items):
    print("*** pytest_collection_modifyitems ***", session, config, items)


def pytest_collection_finish(session):
    print('*** pytest_collection_finish ***', session)


def pytest_runtest_setup(item):
    print("*** pytest_runtest_setup ***", item.name)


def pytest_runtest_teardown(item):
    print("*** pytest_runtest_teardown ***",item.name)


def pytest_sessionfinish(session):
    print("*** pytest_sessionfinish ***", session)


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Mention browser to pick -chrome,ff,edge')




def pytest_addoption(parser):
    parser.addoption("--cmdopt", action='store', default='type1', help='Options: type1 or type2')


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--cmdopt")

