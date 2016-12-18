Pages
#####

Main Page
=========

.. module:: pyman.Main

.. autoclass:: Main
    :show-inheritance:

    .. attribute:: title

        The title to display for all menus

    .. attribute:: chars

        A list of characters to use when displaying the menu.

        * chars[0]: Character to use for the Title Border. Defaults to '='
        * chars[1]: Character to use for the Menu Border. Defaults to '-'
        * chars[2]: Characters to use for each entry in the menu. Defaults to ') '

    .. attribute:: current

        A list that houses the stack of pages.

        This is used then executing the Action :class:`pyman.Actions.Back`

    .. attribute:: current_title

        The current title that is being displayed

    .. attribute:: is_automated

        A boolean that to determines if the CLI is running in automated mode.

        This becomes True if you run pymain.Main.cli() with a list of commands,
        otherwise it is False.

Page Class
==========

.. module:: pyman.Page

.. autoclass:: Page

    .. attribute:: name

        The display name for this page

    .. attribute:: parent

        The parent page to this page

    .. attribute:: menu

        The main page for this CLI instance

    .. attribute:: actions

        This is a list where the attached Actions and Pages are stored

    .. automethod:: init

    .. automethod:: choices

    .. automethod:: add

    .. automethod:: add_action

    .. automethod:: run
