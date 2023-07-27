conda activate expose
cd expose

for d in /mnt/share/NTU/rgb_img_single/train/*;
do
	python rgb2pt.py --img_folder "$d" --exp-cfg data/conf.yaml --show=False --save-mesh False --save-params True
done

for d in /mnt/share/NTU/rgb_img_single/test/*;
do
	python rgb2pt.py --img_folder "$d" --exp-cfg data/conf.yaml --show=False --save-mesh False --save-params True
done
conda deactivate