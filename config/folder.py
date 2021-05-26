import os

base = os.path.dirname(__file__).replace("\\config", "")
dataset = os.path.join(base, 'dataset')

def get_dataset_path(file_name: str):
    """
    /dataset 폴더 내의 파일의 경로 반환
    """
    file_path = os.path.join(dataset, file_name)

    return file_path


