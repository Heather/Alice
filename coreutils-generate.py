#!/usr/bin/python

import os,io,sys
import StringIO

u = """ base32
        base64
        basename
        cat
        cksum
        comm
        cp
        cut
        dircolors
        dirname
        echo
        env
        expand
        expr
        factor
        false
        fmt
        fold
        hashsum
        head
        link
        ln
        ls
        md5sum
        mkdir
        mktemp
        nl
        nproc
        od
        paste
        printenv
        printf
        ptx
        pwd
        readlink
        realpath
        relpath
        rm
        rmdir
        seq
        sha1sum
        sha224sum
        sha256sum
        sha3-224sum
        sha3-256sum
        sha3-384sum
        sha3-512sum
        sha384sum
        sha512sum
        shred
        shuf
        sleep
        sort
        split
        sum
        sync
        tac
        tail
        tee
        test
        tr
        true
        truncate
        tsort
        unexpand
        uniq
        wc
        whoami
        yes """

s = StringIO.StringIO(u)
for line in s:
  line = line.strip()
  with io.FileIO("%s.cmd" % line, "w") as file:
    print(" -> %s.cmd" % line)
    pss = '%'
    cmd = "@echo off\nuutils %s %s*\n" % (line, pss)
    file.write(cmd)
print("complete")
