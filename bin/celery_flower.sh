#!/bin/bash
exec celery flower --app bitvavo_dca --workdir src
