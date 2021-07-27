#!/usr/bin/env bash

main () {
	if [[ $# -ne 1 ]] 
	then echo "Usage: $0 <person>"; exit 1; 
	else
	echo "Hello, $@"
	fi
}
main "$@"
