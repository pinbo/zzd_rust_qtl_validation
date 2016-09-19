# 09/19/2016 split the grouped samples and give them a common number (here is the current line number $.)
perl -F, -ane 'foreach $i (@F) {print "$.\t$i\n";}' organzied_identical_snps.txt | xclip
