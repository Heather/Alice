@echo off
git log `git log -1 --format=%H -- CHANGELOG*`..; cat CHANGELOG*
