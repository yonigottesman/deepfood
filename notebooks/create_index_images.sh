#!/bin/bash
wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
tar -xf food-101.tar.gz
kaggle competitions download -c ifood-2019-fgvc6
unzip ifood-2019-fgvc6.zip
unzip train_set.zip
mkdir index_images
mkdir index_images/dummy_class
find food-101/images -mindepth 2 -type f -exec mv -t index_images/dummy_class -i '{}' +
rsync -r train_set/ index_images/dummy_class
find index_images/dummy_class  -type f -exec mv  {} {}__.jpg \;
cd index_images/dummy_class && ls -v | cat -n | while read n f; do mv -n "$f" "$n.jpg"; done
