import moondream as md
from PIL import Image
from typing import Union

class MoonDreamInitialize:
    #Initialize for Moondream Cloud
    def __init__(self,api_key =None):
        self.model = md.vl(api_key=api_key)

    #Initializing Caption for image
    def description(self , Image : Union[Image.Image, str], detail:str ="normal")->str:
        img =self._load_image(Image)
        caption = self.model.caption(img,length=detail)["caption"]
        return caption
    
    #Query the image 
    def query(self,Image:Union[Image.Image,str], question:str)->str:
        img =self._load_image(Image)
        answer = self.model.query(img,question)["answer"]
        return answer
    
    def point(self, image: Union[Image.Image, str], object: str) -> str:
        img = self._load_image(image)
        point = self.model.point(img, object)
        return point["point"]
    
    def detect(self, image: Union[Image.Image, str], object: str) -> str:
        img = self._load_image(image)
        detect = self.model.query(img, object)
        # Assuming `detect` is a dictionary, format it as a string
        if isinstance(detect, dict):
         return ", ".join(f"{key}: {value}" for key, value in detect.items())
        elif isinstance(detect, list):
            return ", ".join(str(item) for item in detect)
        else:
            return str(detect)

    def _load_image(self, image: Union[Image.Image, str]) -> Image.Image:
        if isinstance(image, str):
            return Image.open(image)
        return image
    
        