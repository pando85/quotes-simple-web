#!/bin/sh
set -e

if [ -z "${VUE_APP_API_URL+x}" ];
then
  echo "please, set API url in envar VUE_APP_API_URL" ;
  exit
fi


## modify default value in minify js
sed -i "s,\"http://localhost:8080\",\"$VUE_APP_API_URL\",g" /usr/share/nginx/html/js/app.*.js

exec "$@"
