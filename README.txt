A tool that uses available system information to provide contextualizing information related to the machine that you are working on.

So far (5/5/13): Parses through .bash_history using the Collections module and tabulates how many times each command has been run, then sorts those by most ran.

TODO(Ryan): Parse timestamps of those commands and graph their usage over time (probably via Graphite or something similar). Flip on timestamping in .bash_history if it's not activated. Dig deeper into various commands (e.g. ssh, scp, make). 

>>>>>>> FIX HOW INDEXING WORKS FOR STRIPPING NON-NAME PART OUT OF WHOAMI CALL
