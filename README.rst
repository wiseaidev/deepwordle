deepwordle
==========

.. image:: https://drive.google.com/uc?export=view&id=1iZvpFYx6DNt8BW3pv9RyXRdqiXX5SdLS
   :target: https://drive.google.com/uc?export=view&id=1iZvpFYx6DNt8BW3pv9RyXRdqiXX5SdLS
   :alt: Deepwordle Console

**deepwordle** is a TUI clone of the famous wordle game powered by Python, Deepgram, Textual, Tweepy, and friends.


1. Configurations
-----------------

1.1. Tweepy:
~~~~~~~~~~~~

1.1.1. Twitter Developer Account:
+++++++++++++++++++++++++++++++++

* Create an account on https://developer.twitter.com/, and click on ``Sign Up``

.. image:: https://drive.google.com/uc?export=view&id=1pgGcVv-YuFZmsjU7KabiM0lQ7kMgQBMe
   :target: https://drive.google.com/uc?export=view&id=1pgGcVv-YuFZmsjU7KabiM0lQ7kMgQBMe
   :alt: Developer Account SignUp

* Fill out the required information and submit your request.

.. image:: https://drive.google.com/uc?export=view&id=1W_x9n7_VXpfV_dskY-7D8UMpJAPtn0r5
   :target: https://drive.google.com/uc?export=view&id=1W_x9n7_VXpfV_dskY-7D8UMpJAPtn0r5
   :alt: Developer Portal

* Once approved, you can continue with the app setup.

.. image:: https://drive.google.com/uc?export=view&id=14d9g_83joI0QoUmU25ZBSdt5Yh7mGzYY
   :target: https://drive.google.com/uc?export=view&id=14d9g_83joI0QoUmU25ZBSdt5Yh7mGzYY
   :alt: Verify Email


Note that you need to provide detailed information about your use case for the API in order to speed up the process of reviewing your request.

1.1.2. Create an App:
+++++++++++++++++++++

Once your request gets approved, you will be prompted to create an app as shown in the image below:

.. image:: https://drive.google.com/uc?export=view&id=17wsWPWNAZqhuALieMOO2SLnOFp6u_hP6
   :target: https://drive.google.com/uc?export=view&id=17wsWPWNAZqhuALieMOO2SLnOFp6u_hP6
   :alt: Create App

Alternatively, you can go to: https://developer.twitter.com/en

* click on the ``developer portal`` panel. By doing so, you will be redirected to your dashboard.



* Navigate to the ``Projects & Apps`` --> ``Overview``, Scroll to the bottom of the page and click on ``Create App``.

.. image:: https://drive.google.com/uc?export=view&id=1U8gb7WDR_BYaA7jVNhKBHMqdlSYVSzrP
   :target: https://drive.google.com/uc?export=view&id=1U8gb7WDR_BYaA7jVNhKBHMqdlSYVSzrP
   :alt: Apps Overview

* Choose an app name and click ``Complete``. By default, the app will be created in read-only mode.

.. image:: https://drive.google.com/uc?export=view&id=1HEz8QpsU-zaK9L2o4bhvPfVTQbcJeK0Q
   :target: https://drive.google.com/uc?export=view&id=1HEz8QpsU-zaK9L2o4bhvPfVTQbcJeK0Q
   :alt: Read only mode

* Add write permissions to the app in order to be able to publish tweets. Navigate to App Settings and scroll down to ``User authentication settings``, then click ``set up``.

.. image:: https://drive.google.com/uc?export=view&id=1SrP1-6U0XiyJVD0ecu6QK3YLgHMBriM8
   :target: https://drive.google.com/uc?export=view&id=1SrP1-6U0XiyJVD0ecu6QK3YLgHMBriM8
   :alt: User authentication settings

* Toggle the ``OAuth 1.0a`` button and change app permissions to ``Read and Write``.

.. image:: https://drive.google.com/uc?export=view&id=1IrWtgMmILPKMxjfAFDgr6wpDB_Z2_U_g
   :target: https://drive.google.com/uc?export=view&id=1IrWtgMmILPKMxjfAFDgr6wpDB_Z2_U_g
   :alt: Read and Write permissions

* Now your app will get its permissions elevated to ``Read and Write``.

.. image:: https://drive.google.com/uc?export=view&id=1LQpDI1zxP5tftPek9FELane4W9bqEs_c
   :target: https://drive.google.com/uc?export=view&id=1LQpDI1zxP5tftPek9FELane4W9bqEs_c
   :alt: Read and Write permissions

Each app is associated with three sets of keys: an API Key, an API Key Secret, and a Bearer Token.

1.1.3. Store secrets:
+++++++++++++++++++++

You need to store keys and secrets of the app as environment variables in order to authenticate and
publish tweets. To do so, open your terminal, and type the following(change each ``XXXXXXXXXX``
value accordingly):

.. code-block:: bash

   export CONSUMER_KEY="XXXXXXXXXX"
   export CONSUMER_SECRET="XXXXXXXXXX"
   export ACCESS_TOKEN="XXXXXXXXXX-XXXXXXXXXX"
   export ACCESS_TOKEN_SECRET="XXXXXXXXXX"


1.2. Deepgram:
~~~~~~~~~~~~~~

1.2.1. Create an API Key:
+++++++++++++++++++++++++

In order to interact with the Deepgram API, you need to grab some keys. To do so, follow along the
`deepgram official docs`_ to create an ``API Key``.

Now, you need to store your ``API Key`` as environment variable in order to authenticate and
transcribe audio data. To do so, open your terminal, and type the following(change the ``XXXXXXXXXX``
value accordingly):

.. code-block:: bash

   export DEEPGRAM_API_KEY="XXXXXXXXXX"


2. Requirements
---------------

2.1. Python Interpreter:
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

Make the interpreter available globally:

.. code-block:: bash

   pyenv global system 3.10.1


2.2. Virtual Environment:
~~~~~~~~~~~~~~~~~~~~~~~~~

To manage and set up Python 3.10.1 in a virtual environment, I recommend using `poetry`_.

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

Now, at any point in the future, you want to use a virtual environment created by poetry, you can look up
for installed virtual environments under :code:`~/.cache/pypoetry/virtualenvs`:

.. code-block:: bash

   ls ~/.cache/pypoetry/virtualenvs

To activate a virtual environment, run the following:

.. code-block:: bash

   source ~/.cache/pypoetry/virtualenvs/<your_virtual_environment_name>/bin/activate


2.3. PortAudio:
~~~~~~~~~~~~~~~

deepwordle depends on :code:`PyAudio` which in turn depends on another library called :code:`portaudio`.
To install portaudio on Linux, run the following:

.. code-block:: bash

   sudo apt-get install portaudio19-dev


3. Installation
---------------

deepwordle is currently available for Linux os. There are two main methods you can use to install and run the game

With :code:`pip`:

.. code-block:: console

   python3 -m pip install deepwordle

With `pipx`_:

.. code-block:: console

   python3 -m pip install --user pipx
   pipx install --python python3 deepwordle

pipx will install and run deepwordle in your terminal, kind of similar to `npx`_ if you are familiar with it.


3. Quickstart
-------------

Having deepwordle installed on your machine, you can run it as a CLI from your terminal:

.. code-block:: console

   deepwordle

or you can use poetry to run the game:

.. code-block:: console

   poetry run deepwordle

4. Components Overview
----------------------

There are four main textual components that build up this game:

* ``rich_text``: a module to create customized text with different fonts and sizes.

.. image:: https://drive.google.com/uc?export=view&id=1AjW91cwX5qlly3erSWQZZSuJSx2FR3Qu
   :target: https://drive.google.com/uc?export=view&id=1AjW91cwX5qlly3erSWQZZSuJSx2FR3Qu
   :alt: rich_text

* ``message``: a widget to display rich text within a textual panel.

.. image:: https://drive.google.com/uc?export=view&id=1c59bdmimQsBdr3okiPGDgugcJLRmV5Pf
   :target: https://drive.google.com/uc?export=view&id=1c59bdmimQsBdr3okiPGDgugcJLRmV5Pf
   :alt: message

* ``letter``: a module to build customized buttons with different fonts, sizes, and styles.

.. image:: https://drive.google.com/uc?export=view&id=1xdkxHZQAvU3JVaFFDr2U2DAmWoMkNHwn
   :target: https://drive.google.com/uc?export=view&id=1xdkxHZQAvU3JVaFFDr2U2DAmWoMkNHwn
   :alt: letter

* ``letters_grid``: the main letters grid of the wordle game.

.. image:: https://drive.google.com/uc?export=view&id=1w5-AuKZVeHrfqtUTzj8NsX8SGZVuBcbQ
   :target: https://drive.google.com/uc?export=view&id=1w5-AuKZVeHrfqtUTzj8NsX8SGZVuBcbQ
   :alt: letters_grid


5. Game Workflow
----------------

a- Enter the game by simply typing ``deepwordle`` on your terminal.

.. image:: https://drive.google.com/uc?export=view&id=1-Xaz1SrlMB0ZKvV8eEjd02xLbLly-kfp
   :target: https://drive.google.com/uc?export=view&id=1-Xaz1SrlMB0ZKvV8eEjd02xLbLly-kfp
   :alt: start game

b- Press ``r`` to record a word for two seconds.

c- You will be prompted to either submit the word by pressing enter or remove the letters by pressing backspace.

.. image:: https://drive.google.com/uc?export=view&id=1UZ06LqL286-8PNq5yQtnNGSEnQAk6CsX
   :target: https://drive.google.com/uc?export=view&id=1UZ06LqL286-8PNq5yQtnNGSEnQAk6CsX
   :alt: enter or backspace

d- Repeat steps ``b`` and ``c`` until you complete the game.

.. image:: https://drive.google.com/uc?export=view&id=17EQGC6mPJ3bYX8ZrRm7CF8xeufhVHMsY
   :target: https://drive.google.com/uc?export=view&id=17EQGC6mPJ3bYX8ZrRm7CF8xeufhVHMsY
   :alt: guesses

e- If you guessed the secret word, you will be asked to press ``t`` to tweet your results.

.. image:: https://drive.google.com/uc?export=view&id=1Mm5ZHPEPBH0ACJWO_aDQ7nrh3jIYFfvo
   :target: https://drive.google.com/uc?export=view&id=1Mm5ZHPEPBH0ACJWO_aDQ7nrh3jIYFfvo
   :alt: tweet


👋 Contribute
-------------

If you are looking for a way to contribute to the project, please refer to the `Guideline`_.

📝 License:
-----------

MIT licensed. See the bundled `licence`_ file for more details.

.. _pipx: https://github.com/pypa/pipx
.. _npx: https://docs.npmjs.com/cli/v7/commands/npx
.. _pyenv: https://github.com/pyenv/pyenv
.. _poetry: https://github.com/python-poetry/poetry
.. _licence: https://github.com/Harmouch101/deepwordle/blob/main/LICENSE
.. _deepgram official docs: https://developers.deepgram.com/documentation/getting-started/authentication/#create-an-api-key
.. _Guideline: https://github.com/Harmouch101/deepwordle/blob/main/CONTRIBUTING.rst
