Actions
#######

Inbuilt Actions
===============

.. module:: pyman.Actions

.. autoclass:: Cmd

    .. attribute:: cmd

        The command to run

.. autoclass:: Back

.. autoclass:: Exit


Action Class
============

The Action Class
----------------

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
