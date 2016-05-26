# Microservices small example

The goal of this project is to show a very basic example of a microservice architecture. A Python service will generate prime numbers and a client written in Ruby will consume them through RabbitMQ.

## Requirements

* Pyton 2.x
* Ruby 2.2.x
* RabbitMQ

## Installation

Run:

    $ bundle install
    $ pip install -r requirements.txt

## Execution

Start the service:

    $ python primes_server.py requests primes

Start the clien:

    $ ruby primes_client.rb primes requests 10
