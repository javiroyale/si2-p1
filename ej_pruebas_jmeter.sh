#!/bin/bash

# 
USUARIOS=(1 5 10 15 50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800 850 900 950 1000 1300 1500 1700 2000)
BASE_DIR="/home/sandorsad/TERCERO/SI 2/si2-p1"
FICHERO="$BASE_DIR/P3-projects.jmx"

for u in "${USUARIOS[@]}"
do
    echo "PRUEBA PARA $u USUARIOS"
    cd "$BASE_DIR/P1-base" && python3 manage.py populate
    cd ..
    /home/sandorsad/Descargas/apache-jmeter-5.6.3/bin/jmeter.sh -n -t "$FICHERO" -Jusers=$u -l "results_$u.jtl" -Jsummariser.name=summary -e -o "output_users_$u"

done