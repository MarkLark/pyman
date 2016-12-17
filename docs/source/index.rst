.. pyman documentation master file, created by
   sphinx-quickstart on Sat Dec 17 19:06:15 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyMan!
=================

PyMan is a small library that allows you to build your own CLI to manage your projects.
This way you do not have to remember commands to run, you simply navigate your CLI to run those commands.

Minimal Example:
================

>>> import pyman
>>> pyman.Main( "PyMan - Menu Example", [
>>>     pyman.Action.Cmd( "Hello World", "echo 'Testing PyMan'" ),
>>>     pyman.Action.Exit()
>>> ]).cli()

Example Output

.. code-block:: console

   ================================================================
                         PyMan - Menu Example
   ================================================================

   Main Menu
   --------------------
   1) Hello World
   2) Exit
   --------------------

   Choice:

How It Works
============
PyMan uses the idea of Pages and Actions. Each page is made up of a number of actions.

You start off by instanciating the 'Main Menu' class, providing the title you wish to display:

>>> menu = pyman.Main( "PyMan - Menu Example" )

From here you add other Pages or Actions

>>> menu.add([
>>>     pyman.Action.Exit()
>>> ])

pyman.Action.Exit is one of the in-built actions. Other inbuilt actions include:

* pyman.Action.Exit()
* pyman.Action.Back()
* pyman.Action.Cmd( <name>, <bash command> )

And finally, you start the CLI with:

>>> menu.cli()

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
