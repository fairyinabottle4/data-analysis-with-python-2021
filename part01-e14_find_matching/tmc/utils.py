import importlib
import sys

from unittest.mock import MagicMock

def load_module(pkg, lang='en'):
    """
    Used to load a module without::

        def main()
            pass

        if __name__ == "__main__":
            main()

    When loaded, runs the code immediately.
    """
    module_not_found = 'File {0} does not exist!'.format(pkg)
    other_exception = 'Running exercise {0} failed. Please make sure that you can run your code.'.format(pkg)
    exit_called = 'Make sure your program does not exit with an exit() command.'

    if lang == 'fi':
        module_not_found = 'Tiedostoa {0} ei löytynyt.'.format(pkg)
        other_exception = 'Tehtävän {0} suorittaminen epäonnistui. '.format(pkg) \
            + 'Varmista, että saat ohjelman suoritettua loppuun.'
        exit_called = 'Varmista, että koodisi ei kutsu exit() komentoa.'

    try:
        return importlib.import_module(pkg)
    except ModuleNotFoundError:
        return AssertionError(module_not_found)
    except Exception:
        return AssertionError(other_exception)
    except SystemExit:
        return AssertionError(exit_called)


def reload_module(module):
    """Runs the module code again, used when no main() defined"""
    if isinstance(module, AssertionError):
        raise module
    importlib.reload(module)


def load(pkg, method, lang='en', err=None):
    """
    Loads a method from a module, doesn't run the code, needs to be called in tests.

    Exercise Example::

        import numpy as np

        def main():
            [print(line) for line in range(4)]

    Test Example::

        module_name="src.filename"
        main = load(module_name, "main")
        def test_lines(self):
            main()
            result = get_out().split('\\n')
            self.assertEqual(len(result), 4, msg="The output should contain exactly four lines!")
    """
    module_not_found = 'Function {1} was not found in file {0}.'.format(pkg, method)
    if lang == 'fi':
        module_not_found = 'Tiedostosta {0} ei löytynyt funktiota {1}.'.format(pkg, method)

    if not err:
        err = module_not_found

    def fail(*args, **kwargs):
        if args:
            raise AssertionError(args[0])
        raise AssertionError(err)

    try:
        return getattr(importlib.import_module(pkg), method)
    except ModuleNotFoundError as mnf:
        return fail(mnf)
    except Exception as e:
        return fail


def get_stdout():
    return sys.stdout.getvalue().strip()


def get_stderr():
    return sys.stderr.getvalue().strip()


def any_contains(needle, haystacks):
    any(map(lambda haystack: needle in haystack, haystacks))


def check_source(module):
    """
    Check that module doesn't have any globals.
    Example::

        def test_no_global(self):
            result, line = check_source(self.module)
            self.assertTrue(result, "Make sure no code is outside functions.\\nRow: " + line)
    """
    source = module.__file__
    allowed = []
    allowed.append("import ")
    allowed.append("from ")
    allowed.append("def ")
    allowed.append("class ")
    allowed.append(" ")
    allowed.append("\t")
    allowed.append("#")
    allowed.append("if __name__")
    with open(source) as file:
        for line in file.readlines():
            if line.strip() == "":
                continue
            ok = False
            for prefix in allowed:
                if line.startswith(prefix):
                    ok = True
            if not ok:
                return (False, line)
        return (True, "")


def spy_decorator(method_to_decorate, name):
    """
    This solution to wrap a patched method comes originally from
    https://stackoverflow.com/questions/25608107/python-mock-patching-a-method-without-obstructing-implementation
    """
    mock = MagicMock(name="%s method" % name)
    def wrapper(self, *args, **kwargs):
        mock(*args, **kwargs)
        return method_to_decorate(self, *args, **kwargs)
    wrapper.mock = mock
    return wrapper

class patch_helper(object):
    """
    patch_helper code copied from Data Analysis with Python.
    Example::

        from tmc.utils import load, get_out, patch_helper

        module_name='src.file_listing'
        ph = patch_helper(module_name)

    In tests file, if you want to patch "src.file_listing.re.compile" use following:
    Example::

        def test_content(self):
            patch(ph('re.compile'), side_effect=re.compile) as c:
                ...
    """

    def __init__(self, module_name):
        import importlib
        self.m = module_name

    def __call__(self, d):
        # import importlib
        parts = d.split(".")
        # If e.g. d == package.subpackage.subpackage2.attribute,
        # and our module is called mystery_data.
        try:
            getattr(importlib.import_module(self.m), parts[-1])   # attribute
            p = ".".join([self.m, parts[-1]])
            # p='src.mystery_data.attribute'
        except ModuleNotFoundError:
            raise
        except AttributeError:
            if len(parts) == 1:
                raise
            try:
                getattr(importlib.import_module(self.m), parts[-2])  # subpackage2.attribute
                p = ".".join([self.m] + parts[-2:])
                # p='src.mystery_data.subpackage2.attribute'
            except AttributeError:
                if len(parts) == 2:
                    raise
                try:
                    getattr(importlib.import_module(self.m), parts[-3])  # subpackage.subpackage2.attribute
                    p = ".".join([self.m] + parts[-3:])
                    # p='src.mystery_date.subpackage.subpackage2.attribute'
                except AttributeError:
                    if len(parts) == 3:
                        raise
                    # package.subpackage.subpackage2.attribute
                    getattr(importlib.import_module(self.m), parts[-4])
                    p = ".".join([self.m] + parts[-4:])
                    # p='src.mystery_date.package.subpackage.subpackage2.attribute'
        return p
