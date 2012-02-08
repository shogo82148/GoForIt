#!/bin/sh

g++ -o q03 q03.cpp
python random_string.py > random.txt
./q03 sony < random.txt > result.txt
diff answer.txt result.txt
