for ((i=0; i<8; i++))
do
	echo 'test #'$i
	cat $i'.in' | ./1058.out
	cat $i'.in' | python 1058.py
done
