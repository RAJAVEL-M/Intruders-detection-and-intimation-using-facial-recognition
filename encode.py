#encode.py
import face_recognition as fr
import pickle
import os

encoded = {}
for dirpath, dnames, fnames in os.walk("./faces"):
    for f in fnames:
        if f.endswith(".jpg") or f.endswith(".png"):
             face = fr.load_image_file("faces/" + f)
             encoding = fr.face_encodings(face)[0]
             encoded[f.split(".")[0]] = encoding
f = open('encodingfile', "wb")
f.write(pickle.dumps(encoded))
f.close()
