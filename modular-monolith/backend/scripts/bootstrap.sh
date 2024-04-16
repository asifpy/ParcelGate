#! /bin/sh
python manage.py reset_db --noinput --close-sessions

python manage.py migrate \
    && echo "\e[32m>>> creating super user\e[0m" \
    && python manage.py createsuperuser --noinput \
    && echo "\e[32m>>> collecting static\e[0m" \
    && python manage.py collectstatic --no-input \
    && echo "\e[32m>>> loading [parcel] fixtures\e[0m" \
    && python manage.py loaddata land_broker_hub/data/parcels.yaml \
    && echo "\e[32m>>> loading [broker] fixtures\e[0m" \
    && python manage.py loaddata land_broker_hub/data/brokers.yaml \
    && echo "\e[32m>>> loading [offer] fixtures\e[0m" \
    && python manage.py loaddata land_broker_hub/data/offers.yaml

exit $?