Inbuilt Pages
#############

Documentation
=============

This page allows you to generate HTML Documentation using Sphinx.

code:

.. code-block:: python

    menu.add([
        pyman.Doc()
    ])

menu:

.. code-block:: console

    ================================================================
                          PyMan - Menu Example
    ================================================================

    documentation
    --------------------
    1) Generate Multi-Page HTML
    2) Generate Single-Page HTML
    3) Clean
    4) Back
    --------------------

    Choice:

VCS - Git
=========

This page allows you to perform git commands on your project

code:

.. code-block:: python

    menu.add([
        pyman.Git()
    ])

menu:

.. code-block:: console

    ================================================================
                          PyMan - Menu Example
    ================================================================

    git
    ------------------------------------------
    1) Commit
    2) Commit File
    3) Add File
    4) Push
    5) History
    6) Back
    ------------------------------------------

    Choice:

NoseTest
========

This page allows you to run Unit Tests using NoseTest

code:

.. code-block:: python

    menu.add([
        pyman.NoseTest()
    ])

menu:

.. code-block:: console

    ================================================================
                          PyMan - Menu Example
    ================================================================

    testing_(python_nosetest)
    ------------------------------------------
    1) Without Stdout
    2) With Stdout
    3) Back
    ------------------------------------------

    Choice:

PyPi
====

This page allows you to package your project and upload it to PyPi

code:

.. code-block:: python

    menu.add([
        pyman.PyPi()
    ])

menu:

.. code-block:: console

    ================================================================
                          PyMan - Menu Example
    ================================================================

    pypi
    ------------------------------------------
    1) Package Source
    2) Package Wheel
    3) Upload
    4) Back
    ------------------------------------------

    Choice:
