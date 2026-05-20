import kagglehub

path = kagglehub.dataset_download(
    "emmarex/plantdisease"
)

print("Downloaded to:", path)