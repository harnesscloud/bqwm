#!/usr/bin/env python

from bqwm.api import create_app

def main(argv=None):
    app = create_app()
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()
