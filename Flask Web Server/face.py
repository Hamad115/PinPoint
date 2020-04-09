import face_recognition
import os

def face_matcher(unknown):
    # print(unknown)
    known_directory = "C:\\Users\\hamad\\Downloads\\Flask Web Server\\images\\known"
    unknown_directory = "C:\\Users\\hamad\\Downloads\\Flask Web Server\\images\\unknown"
    known_image_path = os.listdir(known_directory)
    encoding = []
    for item in known_image_path:
        known_image = face_recognition.load_image_file(known_directory + "\\" + item)
        encoding_list = face_recognition.face_encodings(known_image)
        if encoding_list:
            known_encoding = encoding_list[0]
            encoding.append(known_encoding)
        


    unknown_image = face_recognition.load_image_file(unknown_directory + "\\" + unknown)
    encoding_list = face_recognition.face_encodings(unknown_image)
    if encoding_list:
        unknown_encoding = encoding_list[0]
        encoding.append(unknown_encoding)

        results = face_recognition.compare_faces(encoding, unknown_encoding, tolerance=0.7)

        # print(results)

        for index, item in enumerate(known_image_path):
            if results[index]: 
                return(item)
    
        return None


