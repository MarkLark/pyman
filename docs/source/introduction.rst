Introduction To PyMan
#####################

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

* pyman.Action.Exit()
* pyman.Action.Back()
* pyman.Action.Cmd( <name>, <bash command> )

And finally, you start the CLI with:

.. code-block:: python

    menu.cli()
