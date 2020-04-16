!bin/bash
i=1; 
while [$i -le 999]; do 
touch $i.txt; let i++; 
done