# Analyzer of Getty TXT reports

Just an analyzer of Getty TXT reports to understand better the information I'm getting

## How to contribute to the Analyzer

The Analyzer has been implemented using python3. To develop to Analyzer we recommend to employ [Python Virtualenv]( http://docs.python-guide.org/en/latest/dev/virtualenvs/ ):

```
$ pip3 install virtualenv
Collecting virtualenv
  Downloading virtualenv-15.0.3-py2.py3-none-any.whl (3.5MB)
    100% |████████████████████████████████| 3.5MB 398kB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-15.0.3
```

After that, you need to create a virtualenv for you to develop:

```
$ virtualenv venv
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.5'
New python executable in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/venv/bin/python3.5
Also creating executable in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/venv/bin/python
Installing setuptools, pip, wheel...done.
```

Now it time to install PyBuilder:

* First we activate the virtualenv:

```
$ source venv/bin/activate
```

* Now we install PyBuilder using Pip:

```
$ pip install pybuilder
Collecting pybuilder
  Using cached PyBuilder-0.11.9.tar.gz
Requirement already satisfied: pip>=7.0 in ./venv/lib/python3.5/site-packages (from pybuilder)
Collecting tblib (from pybuilder)
  Using cached tblib-1.3.0-py2.py3-none-any.whl
Requirement already satisfied: wheel in ./venv/lib/python3.5/site-packages (from pybuilder)
Building wheels for collected packages: pybuilder
  Running setup.py bdist_wheel for pybuilder ... done
  Stored in directory: /Users/davidgp/Library/Caches/pip/wheels/04/9c/b3/d2d2194e8911818abdfa1c3c47501a64602714415af28d8da8
Successfully built pybuilder
Installing collected packages: tblib, pybuilder
Successfully installed pybuilder-0.11.9 tblib-1.3.0
(venv)
```

Now it is possible to compile the project:

* Install first the dependencies:

```
$ pyb install_dependencies
PyBuilder version 0.11.9
Build started at 2016-11-11 14:55:00
------------------------------------------------------------
[INFO]  Building alde version 1.0.dev0
[INFO]  Executing build in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde
[INFO]  Going to execute task install_dependencies
[INFO]  Installing all dependencies
[INFO]  Processing batch dependency 'mockito'
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: alde
             Version: 1.0.dev0
      Base directory: /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde
        Environments:
               Tasks: install_dependencies [9623 ms]
Build finished at 2016-11-11 14:55:10
Build took 9 seconds (9637 ms)
```

* Now you can build the project (if you are using Windows, probably the coverage task is going to fail)

```
$ pyb
PyBuilder version 0.11.9
Build started at 2016-11-11 14:57:03
------------------------------------------------------------
[INFO]  Building alde version 1.0.dev0
[INFO]  Executing build in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde
[INFO]  Going to execute task publish
[INFO]  Installing plugin dependency coverage
[INFO]  Installing plugin dependency unittest-xml-reporting
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/src/unittest/python
[INFO]  Executed 1 unit tests
[INFO]  All unit tests passed.
[INFO]  Building distribution in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/target/dist/alde-1.0.dev0
[INFO]  Copying scripts to /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/target/dist/alde-1.0.dev0/scripts
[INFO]  Writing setup.py as /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/target/dist/alde-1.0.dev0/setup.py
[INFO]  Collecting coverage information
[WARN]  coverage_branch_threshold_warn is 0 and branch coverage will not be checked
[WARN]  coverage_branch_partial_threshold_warn is 0 and partial branch coverage will not be checked
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/src/unittest/python
[INFO]  Executed 1 unit tests
[INFO]  All unit tests passed.
[WARN]  Module '__init__' was not imported by the covered tests
[INFO]  Overall coverage is 94%
[INFO]  Overall coverage branch coverage is 100%
[INFO]  Overall coverage partial branch coverage is 100%
[INFO]  Building binary distribution in /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde/target/dist/alde-1.0.dev0
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: alde
             Version: 1.0.dev0
      Base directory: /Users/davidgp/Documents/trabajo/TANGO/repositorios/alde
        Environments:
               Tasks: prepare [2407 ms] compile_sources [0 ms] run_unit_tests [40 ms] package [3 ms] run_integration_tests [0 ms] verify [134 ms] publish [616 ms]
Build finished at 2016-11-11 14:57:06
Build took 3 seconds (3219 ms)
```

Done!

Now, remember, each time you need to start to develop, initalize the virtualenv:

```
$ source venv/bin/activate
```

