FROM postgres

ENV POSTGRES_HOST_AUTH_METHOD=trust

# COPY /scrapeit/result.csv /result.csv
# COPY ./ads_25pg_img2_20221118.csv /ads_25pg_img2_20221118.csv
COPY ./0_init.sql /docker-entrypoint-initdb.d/
COPY ./1_init.sh /docker-entrypoint-initdb.d/