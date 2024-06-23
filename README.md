Junior Python Developer Test Task<br> FastAPI Text Sumarrization

Setup Create a virtual environment:<br>
python -m venv venv<br>
Activate Venv:<br>
source env/bin/activate # On Windows use env\Scripts\activate<br>

Install dependencies:<br>
pip install requirements.txt

Run the application:<br>
uvicorn main:app --reload

Test the endpoint:<br>
Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.

EXAMPLE using POSTMAN: 
![Postman_GURXJb8sMc](https://github.com/Andreyka121/FastAPI-Text-Summarizer/assets/134810272/8f0014ad-39c8-480e-a5c4-9c221dd639c3)
