#!/usr/bin/python
import pyman


pyman.Main( "pyman - Manage", [
    pyman.Doc(),
    pyman.PyPi(),
    pyman.NoseTest(),
    pyman.Git(),
    pyman.Actions.Exit()
]).cli()
