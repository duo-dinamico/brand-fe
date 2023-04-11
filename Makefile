SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

up: ## Run the application
	poetry run flask --app brands run --debug

help: ## Display this help message
	@awk -F '##' '/^[a-z_]+:[a-z ]+##/ { print "\033[34m"$$1"\033[0m" "\n" $$2 }' Makefile
