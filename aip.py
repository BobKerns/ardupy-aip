import sys

from aip.main import main

try:
    main()
except Exception as e:
    sys.stderr.write(str(e) + "\n")
    exit(1)
