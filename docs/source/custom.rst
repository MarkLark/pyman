Custom Page & Action
####################


Page
----

To create your own custom page, you only need to implement two methods in your class, __init__ and init.

.. code-block:: python

    from pyman import Page, Actions

    class MyPage( Page ):
        def __init__( self ):
            super( MyPage, self ).__init__( "My Custom Page" )

        def init( self ):
            self.add([
                Actions.Cmd( "Generate Multi-Page HTML", "cd docs; make html; cd .." ),
                Actions.Cmd( "Generate Single-Page HTML", "cd docs; make singlehtml; cd .." ),
                Actions.Cmd( "Clean", "cd docs; make clean; cd .." ),
                Actions.Back()
            ])


Action
------

To create your own custom Action, you only need to implement the run method.

.. code-block:: python

    from pyman.Action import Action
    class MyAction( Action ):
        def run( self ):
            print "Custom functionality goes here"
