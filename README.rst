Scripts
=======

Installation
------------

.. code:: bash

   git clone https://github.com/terrencetec/scripts.git
   cd scripts
   ./install

Last line will create symbolic link all scripts from scripts/bin to your
``$HOME/.local/bin/``

If you wish to overwrite existing scripts in ``$HOME/.local/bin/``, then
use

.. code:: bash

   ./install -f

instead.


Create new scripts
------------------

Put all your scripts into scripts/bin and make them executable.


Available scripts
-----------------

- ``remove-qtile-default-groups``: remove qtile group a, s, d, f, u, i, o, p
