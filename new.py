import google.generativeai as genai
import json
import PIL.Image



def store_data(input_text, intent_text):
    
    format_data = {
            "Question" : input_text,
            "Answer"  : intent_text
        }
    
    return format_data


def Jarvis( input_text):
    
    genai.configure(api_key="AIzaSyDLfKSSEKLpTJfV_qZWbCyo4m09wOGxxLU")

    model = genai.GenerativeModel('gemini-2.0-flash')

   
    com = model.start_chat()
    intent = com.send_message(input_text)
    final = store_data(input_text=input_text,intent_text=intent.text)
    with open("data.json", "r") as file:
      main = json.load(file)
    
    
    json_data = []
    
    
    for i in range(0,len(main)):
       json_data.append(main[i])
    json_data.append(final)
    print(json_data)
    with open("data.json","w") as  file:
       json.dump(json_data,file,indent=4)
    
    
    return intent.text
    

def jarvis_vision(input,image : str):
   genai.configure(api_key="AIzaSyDLfKSSEKLpTJfV_qZWbCyo4m09wOGxxLU")
   model = genai.GenerativeModel('gemini-1.5-pro-latest')
   image = PIL.Image.open(image)
   exe = model.generate_content([input,image])
   return exe.text
   
