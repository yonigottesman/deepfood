# from torchvision import datasets, models, transforms
# import torch.nn as nn
# import torch as torch
# from annoy import AnnoyIndex


# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# image_size = 224
# std,mean = [0.229, 0.224, 0.225],[0.485, 0.456, 0.406] # pretrained models used these values

# transform = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=mean,
#     std=std)
# ])

# model = models.resnet34(pretrained=False)
# num_ftrs = model.fc.in_features
# model.fc = nn.Linear(num_ftrs, 251)
# model = model.to(device)
# model = nn.DataParallel(model).to(device)

# model.module.load_state_dict(torch.load('app/models/model.pt',map_location=torch.device('cpu'))) # TODO change to Path
# model.eval()

# class EmbeddingExtractor:
#     def sniff_output(self,model, input, output):
#         self.embeddings=output  
#     def __init__(self,model):
#         self.model = model
#         self.model.eval()
#         layer = self.model._modules.get('avgpool')
#         self.handle = layer.register_forward_hook(self.sniff_output)
#     def get_embeddings(self, input):     
#         image = transform(input)
#         with torch.no_grad():
#             self.model(image.to(device).unsqueeze(0))
#         return self.embeddings.squeeze(-1).squeeze(-1).squeeze(0)
    
    
# extractor = EmbeddingExtractor(model.module)

# ann_index = AnnoyIndex(512, 'euclidean')
# ann_index.load('app/models/index.ann')