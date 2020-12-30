## init: init vault
init:
	@echo init vault...
	pip install deepmerge toml
	ssh-keygen -f keys/rsa.key
	ssh-keygen -m pem -f keys/rsa.key
	openssl rsa -in ./keys/rsa.key -pubout -outform pem > ./keys/rsa.key.pub
	@echo done

## bake: bake vault
bake:
	@python3 ./bin/bake.py
	@echo done

## unbake: unbake vault
unbake:
	@python3 ./bin/unbake.py
	@echo done

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run with parameter options: "
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
