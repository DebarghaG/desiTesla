for file in F*png
do
   mv "$file" "${file:2}"
done