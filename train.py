import cv2
import face_recognition
import pandas as pd
import numpy as np
from sql import engine
from flask import render_template
import io
from PIL import Image

classNames = []
encodeListKnown = []
def trains():
    import io
    from PIL import Image
    query = """
                SELECT * FROM attendace_database.images_for_training
            """
    df = pd.read_sql(query, engine)
    images = []
    a = []
    for row in df.itertuples():
        image = Image.open(io.BytesIO(row[2]))
        image = np.asarray(image)
        images.append(image)
        a.append(row[1])

    print("NO OF FACES IN FOLDER ARE :", len(a))
    global classNames
    classNames = a
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    c = findEncodings(images)
    global encodeListKnown
    encodeListKnown = c
    print('Encoding Complete')

