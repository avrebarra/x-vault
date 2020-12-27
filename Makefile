## bake: bake vault
bake:
	@echo unimplemented

## unbake: unbake vault
unbake:
	@echo unimplemented

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run with parameter options: "
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo
