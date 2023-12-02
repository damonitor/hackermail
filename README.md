hackermail
==========

hackermail is a mail client for hackers who collaborate using mailing lists.
Using hackermail, you can fetch mailing list archives, read mails in those, and
write replies or new mails.

For now, hackermail supports only public-inbox[1] managed mailing list
archives.  Linux Kernel Mailing Lists (LKML)[2] are good examples.

[1] https://public-inbox.org/design_notes.html<br>
[2] https://www.kernel.org/lore.html


Quick Tutorials
===============

List mails in damon mailing list (https://lore.kernel.org/damon) which were
sent within last three days:

    $ ./hkml init --manifest ./manifests/lore.js
    $ ./hkml ls damon --fetch

Read the content of 5th mail in the list:

    $ ./hkml ls damon --range 5

Send a reply to the mail:

    $ ./hkml ls damon --range 5 --reply

Write a mail to the mailing list, and send:

    $ ./hkml write --cc damon@lists.linux.dev --open_editor --send

For more detail,

    $ ./hkml -h


Working Directory
=================

Hackermail needs a directory to save the fetched mails and its metadata.  You
may think this as something similar to '.git' directory of git.

You can explicitly set the path to the directory using 'HKML_DIR' environment
variable, or '--hkml_dir' command option.  If the path is not specified,
hackermail assumes the directory is named as '.hkm' and placed under current
directory, the 'hkml' executable file placed directory, or your home directory
and try to find it.


Manifest File
=============

hackermail manifest file describes from where in the internet the mails you
want to read can be fetched, name of the mailing lists archived in the site,
and the site-relative path to the git repositories for each mailing list in
json format.  It's very similar to that of lore[1].  A sample manifest file for
the linux kernel mailing lists is located at 'manifests/lore.js'.  It's
retrieved by 'update_lore_manifest.sh'.

You can explicitly set the path to the manifest file using '--manifest' option
of relevant subcommands.  If it is not specified, hackermail assumes it is
placed under the working directory in name of 'manifest' and try to use it.

[1] https://www.kernel.org/lore.html


Author
======

SeongJae Park <sj38.park@gmail.com>