let x = read_int() in
let y = read_int() in
let z = read_int() in
print_string "Le plus petit est : ";
if x < y
then
  begin
  if x < z
     then print_int x
     else print_int z;
  end
else
  begin
  if y < z
     then print_int y
     else print_int z;
  end
;