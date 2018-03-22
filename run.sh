#!/usr/bin/env bash
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
export FLASK_DEBUG=True
export FLASK_APP=basic_app/__init__.py
flask run --host 127.0.0.1 --port 8088 --with-threads
