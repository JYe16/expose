conda activate expose

# for d in /mnt/h/Datasets/NTU/rgb_img_single/train/*;
# do
# 	python rgb2pt.py --img-folder $d --show=False --save-mesh False --save-params True --output-folder /mnt/h/Datasets/NTU/params_single/
# done

for d in /mnt/h/Datasets/NTU/rgb_img_single/test/*;
do
	file="/mnt/h/Datasets/NTU/params_single/test/"${d##*/}".pt"
	# echo "$file"
	if [ -e "$file" ]
	then
		echo "File exists"
	else
		python rgb2pt.py --img-folder $d --show=False --save-mesh False --save-params True --output-folder /mnt/h/Datasets/NTU/params_single/
	fi
done

conda deactivate
