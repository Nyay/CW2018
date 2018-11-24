#!/usr/bin/env python3

import sys
sys.path.insert(0, '/home/dtatarinov/folklore_corpus')
sys.path.insert(0, '/home/dtatarinov/folklore_corpus/app')

from app import app as application

if __name__ == '__main__':
    application.run(debug=True, port=5001)

