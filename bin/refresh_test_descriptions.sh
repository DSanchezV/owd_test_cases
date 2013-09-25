#!/bin/bash
#
# Refreshes the test description file (or just adds missing descriptions).
#
# Parameters: "Y" if you only want to add missing descriptions.
#
CURRDIR=$(pwd)
THISDIR=$(dirname $0)
DESC_FILE=$THISDIR/../Docs/test_descriptions
ID_LIST=$(find $THISDIR/../tests -name "test_*.py" | sed -e "s/^.*test_\([^\.]*\).*$/\1/")

printf "\nFetching descriptions for new tests: "
cp $DESC_FILE $DESC_FILE.new

#
# Based on what the user wanted, get the descriptions.
#
DONESOME=""
while read num
do
	[ ! "$num" ] && continue

    if [ "$1" ]
    then
        #
        # User only wants to add missing descriptions.
        #
        x=$(egrep "^$num\|" $DESC_FILE)
        if [ "$x" ]
        then
            continue
        fi
    fi

    DONESOME="Y"
    printf "."
    echo "$num|$($THISDIR/get_test_description.sh $num)" >> $DESC_FILE.new 2>/dev/null

    # (In case there is a problem...)
    [ $? -ne 0 ] && exit 1

done <<EOF
$(echo "$ID_LIST")
EOF

if [ ! "$DONESOME" ]
then
    printf "(no tests found to be processed).\n\n"
else
    printf " done.\n"

    #
    # Sort the description file in order of test case ID and replace the original with it.
    #
    sort -t"|" -n -k1 $DESC_FILE.new > $DESC_FILE
    rm $DESC_FILE.new

    echo ""
fi
