FROM php:7.4-apache

RUN apt-get update && \
    apt-get install -y libonig-dev

RUN docker-php-ext-install pdo_mysql mysqli
