# Deepfood - Image Retrieval System in Production
Blog post on this project: [https://yonigottesman.github.io/2020/05/15/deep-search-aws.html](https://yonigottesman.github.io/2020/05/15/deep-search-aws.html)

System Arcitecture
--
![](https://github.com/yonigottesman/deepfood/blob/master/images/image_search_arch.png)

Project Structure
--
#### Starlette web app
[Web application](https://github.com/yonigottesman/deepfood/tree/master/deepfood_service) that receives an image from user and return most similar images from index.

#### Training and Indexing Scripts
- [Notebook](https://github.com/yonigottesman/deepfood/blob/master/notebooks/train_model.ipynb) that fine tunes resnet34 pretrained model on food images.
- [Notebook](https://github.com/yonigottesman/deepfood/blob/master/notebooks/create_index.ipynb) that creates Annoy index.
- [Script](https://github.com/yonigottesman/deepfood/blob/master/notebooks/create_index_images.sh) that creates single folder with all images to index.
- [Notebbok](https://github.com/yonigottesman/deepfood/blob/master/notebooks/embeddings.ipynb) to better understand embeddings.



