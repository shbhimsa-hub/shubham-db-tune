FROM alpine:latest

RUN apk add --no-cache \
  perl \
  perl-utils \
  nginx \
  curl \
  bash \
  git \
  tar

# Download and install pgBadger
RUN curl -L https://github.com/darold/pgbadger/archive/refs/heads/master.tar.gz -o pgbadger.tar.gz && \
    tar -xzf pgbadger.tar.gz && \
    cd pgbadger-master && \
    install -m 755 pgbadger /usr/local/bin/pgbadger && \
    cd .. && rm -rf pgbadger*

COPY nginx.conf /etc/nginx/nginx.conf

CMD sh -c "mkdir -p /var/www/html && \
  pgbadger -f stderr -o /var/www/html/index.html /var/log/postgresql/postgresql.log && \
  while true; do sleep 3600; pgbadger -f stderr -o /var/www/html/index.html /var/log/postgresql/postgresql.log; done & \
  nginx -g 'daemon off;'"

