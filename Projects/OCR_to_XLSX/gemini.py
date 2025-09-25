import os
import pandas as pd
from io import StringIO, BytesIO
from google import genai
from google.genai import types
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
       Act like a professional OCR assistant. Your role is to read text from a provided image and accurately reconstruct it into a structured CSV table.

Objective:
Extract all table data precisely, ensuring that every detected cell—even complex entries such as "1*3S" or "10S"—is captured exactly as it appears. Preserve numbers, letters, symbols, units, and multipliers without alteration, abbreviation, or omission.

Step-by-step instructions:

1. Detect the table from the image and reconstruct it with clear rows and columns.
2. Do not merge columns under any circumstances. Each column should remain separate.
3. Handle missing headers:
   - Prefer keeping the header cell blank (an empty string).
   - If that fails, label it as "Unnamed".
4. Ensure that all values (numbers, text, symbols, units, multipliers, alphanumeric strings) are captured exactly.
5. Maintain strict alignment so that every cell is placed under the correct column.
6. Output format: CSV only. Do not add explanations, comments, extra formatting, or surrounding text.
7. Example schema (subject to change depending on input):
   ITEM NAME,DOSAGE,RATE,OPENING QTY.,OPENING VALUE,RECEIPT QTY.,RECEIPT VALUE,ISSUE QTY.,ISSUE VALUE,CLOSING QTY.,CLOSING VALUE,DUMF QTY.

Dosage/Unit Rules:
8. Carefully read numeric prefixes: "1S", "10S", "5ML", "150ML", etc.
9. Preserve asterisk multipliers exactly (e.g., "1*3S").
10. Do not merge numbers with letters incorrectly.
11. When unsure about zeros, tens, or small letters, prefer the format: NUMBER + UNIT (e.g., "10S" not "1S").
12. Common patterns: XS, X*YS, XML, XGM, XG.

Context Verification:
13. Compare extracted values to typical medicine units.
14. If a dosage seems unusually small or inconsistent with the ITEM NAME (e.g., "MICROFLORA V CAP"), check for missing digits and preserve the intended quantity.

Reference Examples (for guidance only):
ITEM NAME,DOSAGE
AMINORICH,CAP 1S
MICROFLORA V,CAP 10S
INOCQD MAX,GRANULES 1S

        """

        response = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt,imge],config=types.GenerateContentConfig(
            temperature=0.4
        ))

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
