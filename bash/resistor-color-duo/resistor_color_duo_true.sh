#!/usr/bin/env bash

main () {
	for arg in "$1" "$2"; do
		case $arg in
			black) echo -n "0";;
			brown) echo -n "1";;
			red) echo -n "2";;
			orange) echo -n "3";;
			yellow) echo -n "4";;
			green) echo -n "5";;
			blue) echo -n "6";;
			violet) echo -n "7";;
			grey) echo -n "8";;
			while) echo -n "9";;
			*) echo "invalid color" ; return 1;;
		esac
	done
	echo ""
}

main "$@"
