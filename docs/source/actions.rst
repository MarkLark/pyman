Actions
#######

Each page is made up of a list of actions.

An action can be one of the inbuilt actions, a Page, or your own custom Action.

Inbuilt Actions
===============

Terminal Command
----------------

This command allows you to execute a command in the terminal

.. code-block:: python

    menu.add([
        pyman.Actions.Cmd( "Hello World", "echo 'Hello World'" )
    ])

.. module:: pyman.Actions

.. autoclass:: Cmd
    :show-inheritance:

    .. attribute:: cmd

        The command to run

Back
----

This command will send you back one page in the menu

.. code-block:: python

    menu.add([
        pyman.Actions.Back()
    ])

.. autoclass:: Back
    :show-inheritance:

Exit
----

This command will exit out of the CLI

.. code-block:: python

    menu.add([
        pyman.Actions.Exit()
    ])

.. autoclass:: Exit
    :show-inheritance:


Action Class
============

.. module:: pyman.Action

.. autoclass:: Action

    .. attribute:: name

        The display name for this action

    .. attribute:: parent

        The parent page this action is assigned to, value assigned when added to a Page

    .. attribute:: menu

        The main page for this CLI instance, value assigned when added to a Page

    .. automethod:: init

    .. automethod:: run
