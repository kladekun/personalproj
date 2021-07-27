#!/usr/bin/env bash

main () {
read -r black brown red orange yellow green blue violet grey white <<< "0 1 2 3 4 5 6 7 8 9"
declare -A colour=( [black]=1 [brown]=1 [red]=1 [orange]=1 [yellow]=1 [green]=1 [blue]=1 [violet]=1 [grey]=1 [white]=1 )
export black brown red orange yellow green blue violet grey white
if [[ ${colour[$1]} != 1 || ${colour[$2]} != 1 ]]; then
        echo "invalid color"; exit 1
fi
echo ${!1}${!2}
}
main "$@"
