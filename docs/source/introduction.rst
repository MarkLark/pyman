Introduction To PyMan
#####################

PyMan is a small library that allows you to build your own CLI to manage your projects.
This way you do not have to remember commands to run, you simply navigate your CLI to run those commands.

Installing
==========

PyMan is available from the PyPi repository.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install pyman
    Collecting pyman
      Using cached pyman-0.1.0a1-py2.py3-none-any.whl
    Installing collected packages: pyman
    Successfully installed pyman-0.1.0a1

Minimal Example
===============

.. code-block:: python

    import pyman

    pyman.Main( "PyMan - Menu Example", [
        pyman.Action.Cmd( "Hello World", "echo 'Testing PyMan'" ),
        pyman.Action.Exit()
    ]).cli()

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

.. code-block:: python

    menu = pyman.Main( "PyMan - Menu Example" )

From here you add other Pages or Actions

.. code-block:: python

    menu.add([
        pyman.Action.Exit()
    ])

pyman.Action.Exit is one of the in-built actions. Other inbuilt actions include:

* :class:`pyman.Actions.Cmd`
* :class:`pyman.Actions.Back`
* :class:`pyman.Actions.Exit`

And finally, you start the CLI with:

.. code-block:: python

    menu.cli()
