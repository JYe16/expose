conda activate expose
cd expose
for f in ~/Code/smplx_convert/data/rgb_ntu_selected/*;
do
	name=$(basename $f)
	python vid2img_ntu.py --file $name
done
cd ..
conda deactivate
