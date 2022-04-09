deepwordle
==========

**deepwordle** is a TUI clone of the famous wordle game powered by Python, Deepgram, Textual, Tweepy and friends.

1. Requirements
---------------

1.1. Python Interpreter:
~~~~~~~~~~~~~~~~~~~~~~~~

**deepwordle** was tested and built with Python 3.10.1.

To install Python 3.10.1, I recommend using `pyenv`_.

.. code-block:: bash

   git clone https://github.com/pyenv/pyenv ~/.pyenv

Configure `pyenv` on zsh:

.. code-block:: bash

   cat << EOF >> ~/.zshrc
   # pyenv config
   export PATH="${HOME}/.pyenv/bin:${PATH}"
   export PYENV_ROOT="${HOME}/.pyenv"
   eval "$(pyenv init -)"
   EOF

Or if you are using the default bash shell, run the following command instead:

.. code-block:: bash

   cat << EOF >> ~/.bashrc
   # pyenv config
   export PATH="${HOME}/.pyenv/bin:${PATH}"
   export PYENV_ROOT="${HOME}/.pyenv"
   eval "$(pyenv init -)"
   EOF

Close your terminal and open a new shell session. Now, you can install `Python3.10.1`.

.. code-block:: bash

   pyenv install 3.10.1

Make the intrepeter available globally:

.. code-block:: bash

   pyenv global system 3.10.1


1.2. Virtual Environment:
~~~~~~~~~~~~~~~~~~~~~~~~~

To manage and setup Python 3.10.1 in a virtual environment, I recommend using `poetry`_.

You can install poetry by running the following command:

.. code-block:: bash

   curl -sSL https://install.python-poetry.org | python3 -

To test if everything was installed correctly, run the following:

.. code-block:: bash

   poetry env use 3.10.1

However, if you are using virtualenv installed via apt, you are most likely to run into
the following:

.. code-block:: bash

   Creating virtualenv deepwordle-dxc671ba-py3.10 in ~/.cache/pypoetry/virtualenvs

   ModuleNotFoundError

   No module named 'virtualenv.seed.via_app_data'

   at <frozen importlib._bootstrap>:973 in _find_and_load_unlocked

To resolve this issue, you need to reinstall virtualenv through pip:

.. code-block:: bash

   sudo apt remove --purge python3-virtualenv virtualenv
   python3 -m pip install -U virtualenv

Having virtualenv set up, you can use poetry to create a new project along with a virtual environment:

.. code-block:: bash

   poetry new deepwordle && cd deeepwordle

Now, you need to let poetry know which version of python to run:

.. code-block:: bash

   poetry env use 3.10.1

Then, you can create and activate a virtual environment to use for this project:

.. code-block:: bash

   poetry shell

Now, at any point in the future you want to use a virtual environment created by poetry, you can look up 
for installed virtual environments under :code:`~/.cache/pypoetry/virtualenvs`:

.. code-block:: bash

   ls ~/.cache/pypoetry/virtualenvs  

To activate a virtual environment, run the following:

.. code-block:: bash

   source ~/.cache/pypoetry/virtualenvs/<your_virtual_environment_name>/bin/activate


1.3. PortAudio:
~~~~~~~~~~~~~~~

deepwordle depends on :code:`PyAudio`: which in turn depends on another library called :code:`portaudio`.
To install portaudio on linux, run the following:

.. code-block:: bash

   sudo apt-get install portaudio19-dev


2. Installation
---------------

deepwordle is currently available for linux os. There are two main methods you can use to install and run the game

With :code:`pip`:

.. code-block:: console

   python3 -m pip install deepwordle

With `pipx`_:

.. code-block:: console

   python3 -m pip install --user pipx
   pipx install --python python3 deepwordle

pipx will install and run deepwordle in your terminal, kind of similar to `npx`_ if you are familiar with.

.. _pipx: https://github.com/pypa/pipx
.. _npx: https://docs.npmjs.com/cli/v7/commands/npx
.. _pyenv: https://github.com/pyenv/pyenv
.. _poetry: https://github.com/python-poetry/poetry