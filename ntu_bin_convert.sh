conda activate expose
cd expose
for f in ~/Code/smplx_convert/data/rgb_ntu_selected/*;
do
	name=$(basename $f)
	python vid2img_ntu.py --file $name
done

for d in ~/Code/smplx_convert/data/img_ntu_selected/*;
do
	python rgb2pt_ntu.py --image-folder $d --exp-cfg data/conf.yaml --show=False --save-mesh True
done
cd ..
rm -r img_ntu_selected/*
conda deactivate
