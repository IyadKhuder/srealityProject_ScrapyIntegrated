#!/bin/bash

# psql -c "\copy aptads FROM '/ads_25pg_img2_20221118.csv' delimiter ',' csv"
psql -c "\copy aptads FROM 'result.csv' delimiter ',' csv"