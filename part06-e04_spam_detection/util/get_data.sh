#!/bin/bash

curl -O https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham.tar.bz2
curl -O https://spamassassin.apache.org/old/publiccorpus/20030228_spam.tar.bz2

tar -jvxf 20030228_easy_ham.tar.bz2
tar -jvxf 20030228_spam.tar.bz2


rm spam/cmds easy_ham/cmds

ls spam/* | while read f ; do sed -n '/^Subject:/p;/^$/,$p' $f | tr -c -d '[:print:]' | sed 's/[       ]\+/ /g' ; echo ; done > spam.txt

ls easy_ham/* | while read f ; do sed -n '/^Subject:/p;/^$/,$p' $f | tr -c -d '[:print:]' | sed 's/[       ]\+/ /g' ; echo ; done > ham.txt
