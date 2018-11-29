#!/bin/bash

#lists the contents of the current directory in an html and opens it

#set output of ls to 
ls_string="$(ls)"
head_string="<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"></head>"
out_string="$head_string<body><div>${ls_string//[[:space:]]/<br/>}</div></body></html>"
touch out.html
echo $out_string > out.html
xdg-open out.html &

