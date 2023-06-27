conda activate expose
cd expose
for d in /media/persec/Data/yzk/img_ntu_selected/*;
do
	# echo $d
	python rgb2pt_ntu.py --image-folder $d --exp-cfg data/conf.yaml --show=False --save-mesh True
done
cd ..
rm -r /media/persec/Data/yzk/img_ntu_selected/*
conda deactivate
