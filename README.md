# IP Locator

## Description

IP Locator is a web application that provides physical location of ip addresses based on the free database provided by [MAXMIND](https://dev.maxmind.com/geoip/geoip2/geolite2/).

## Technology Stack

* Flask
* Docker
* Redis

## Manual

* Pre-build:
  * Clone the repo
  * `cd` to the repo
* Build: 
  * `docker-compose build`
  * optional: use `--no-cache`
* Run: `docker-compose up`
