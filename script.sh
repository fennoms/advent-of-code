#!/bin/bash

# Put this script in your ~/.bash_aliases file. The script has three commands:
# aoc-load <year> <day>: load the input data for the given year and day.
# aoc-run <year> <day>: run the program for the given year and day on the real input (input.txt)
# aoc-test <year> <day>: run the program for the given year and day on the test input (test.txt)
# If no arguments are given, it defaults to today.

# Function to get the current year or a specified year
function get-year() {

    local year=$(date +%Y)

    # Override year if argument given
    if [ -n "$1" ]; then
        year=$1
    fi

    echo $year
}

# Function to get the current day or a specified day
function get-day() {

    local day=$(date +%d)

    # Override day if argument given
    if [ -n "$1" ]; then
        day=$1
    fi

    echo $day
}

# Get the session cookie from Advent of Code
SESSION=""
# Directory of Advent of Code repository
AOC="$HOME/Documents/advent-of-code"

# Function to run the Python solution for a specified year and day using the real input (input.txt)
function aoc-run() {
    YEAR=$(get-year $1)
    DAY=$(get-day $2)

    cd $AOC/$YEAR/$DAY
    python3 solution.py < input.txt
    cd $AOC
}

# Function to run the Python solution for a specified year and day using the test input (test.txt)
aoc-test() {
    YEAR=$(get-year $1)
    DAY=$(get-day $2)

    cd $AOC/$YEAR/$DAY
    python3 solution.py < test.txt
    cd $AOC
}

# Function to download the input data for a specified year and day from the Advent of Code website
function aoc-load() {
    YEAR=$(get-year $1)
    DAY=$(get-day $2)

    cd $AOC
    mkdir -p $YEAR/$DAY
    cd $YEAR/$DAY

    curl -b "session=$SESSION" https://adventofcode.com/$YEAR/day/$DAY/input > input.txt
    cd $AOC
}
