#!/bin/bash

function prompt {
    local GREEN="\033[32m"
    local RED="\033[91m"
    local CYAN="\033[36m"
    local NONE="\033[0m"

    case $1 in
        "-g")
            echo -e "$GREEN$2$NONE"
            ;;
        "-r")
            echo -e "$RED$2$NONE"
            ;;
        "-c")
            echo -e "$CYAN$2$NONE"
            ;;
    esac
}

function main {
    if [ $# -gt 0 ]
    then
        prompt -r "this function takes no arguments!"
        exit 1
    else
        prompt -c "enter your name:"
        read name
        prompt -c "enter your email:"
        read email
        prompt -c "enter your twitter handle:"
        read handle
        prompt -c "enter your website:"
        read website

        curl 'http://127.0.0.1:8000' -X POST --data-urlencode "name=$name" --data-urlencode "email=$email" --data-urlencode "website=$website" --compressed
        exit 0
    fi
}

main "$@"
