#!/bin/bash

FILEINPUT="../SD_addr.txt"
FILEOUTPUT="../SDtoID.txt"
FILEMAP="../MapSD.txt"

grep -f "$FILEINPUT" "$FILEMAP" > "$FILEOUTPUT"