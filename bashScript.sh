declare -A counters

for file in *; do
  if [[ -f "$file" && "$file" != *.sh ]]; then
    extension="${file##*.}"
    
    if [[ -z "${counters[$extension]}" ]]; then
      counters[$extension]=1
    fi
    
    new_name="${counters[$extension]}.$extension"
    
    while [[ -e "$new_name" ]]; do
      counters[$extension]=$((counters[$extension] + 1))
      new_name="${counters[$extension]}.$extension"
    done
    
    mv "$file" "$new_name"
    
    counters[$extension]=$((counters[$extension] + 1))
  fi
done

echo "Done."