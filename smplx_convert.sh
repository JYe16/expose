conda activate expose38
cd expose
for f in /mnt/Data/Datasets/Own/RGB/*;
do
	name=$(basename $f)
	python vid2img.py --file $name
done

for d in /mnt/Data/Datasets/Own/img/*;
do
	python rgb2pt.py --image-folder $d --exp-cfg data/conf.yaml --show=False --save-mesh True
done
conda deactivate
