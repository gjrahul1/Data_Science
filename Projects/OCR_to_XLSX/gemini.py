import os
import pandas as pd
from io import StringIO, BytesIO
from google import genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

class GeminiProcessor:
    def __init__(self, image_file):
        self.image_file = image_file
        
    def generate_table(self):
        imge = Image.open(self.image_file)
        client = genai.Client(api_key=gemini_api_key)
        prompt = """
        Role: You are an OCR assistant. Your job is to read text from the given image and convert it into a clean structured table.

        Instructions:
        - Identify rows and columns properly.
        - If the image contains tabular data, reconstruct it as a proper table.
        - Output only the table in CSV format (no extra text).
        """

        response = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt,imge])

        return response.text


    def save_to_excel(self,data,filename="output.xlsx"):
        lines = data.splitlines()
        start_row = 0
        for i, line in enumerate(lines):
            if line.strip():
                no_of_commas = line.count(',')

                if no_of_commas >= 2:
                    start_row = i
                    break
           
        df = pd.read_csv(StringIO(data),
        engine="python",
        skiprows=start_row,
        header=None)
        
        df.columns = df.iloc[0]
        df = df[1:]
        
        output = BytesIO()
        df.to_excel(output,index=False)

        return output.getvalue()