conda activate expose
cd expose

for d in /mnt/Data/Datasets/Own/img/*;
do
	python rgb2pt.py --root_path  --image-folder $d --exp-cfg data/conf.yaml --show=False --save-mesh True
done
conda deactivate