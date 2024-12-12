def get_file_extension(text):
    if "python file" in text :
        ex = ".py"
    elif "java file" in text :
        ex = ".java"
    elif "text file" in text:
        ex = ".txt"
    elif "HTML file" in text :
        ex = ".html"
    elif "CSS file" in text:
        ex = ".css"
    elif "JavaScript file" in text:
        ex = ".js"
    elif "JSON file" in text:
        ex = ".json"
    elif "XML file" in text:
        ex = ".xml"
    elif "CSV file" in text:
        ex = ".csv"
    elif "markdown file" in text:
        ex = ".md"
    elif "yaml file" in text:
        ex = ".yaml"
    elif "image file" in text:
        ex = ".jpg"
    elif "video file" in text:
        ex = ".mp4"
    elif "audio file" in text:
        ex = ".mp3"
    elif "PDF file" in text:
        ex = ".pdf"
    elif "word file" in text:
        ex = ".docx"
    elif "excel file" in text:
        ex = ".xlsx"
    elif "powerpoint file" in text:
        ex = ".pptx"
    elif "zip file" in text:
        ex = ".zip"
    elif "tar file" in text:
        ex = ".tar"
    else:
        ex = ""
    return ex

def update_text(text):
    if "python file" in text:
        text = text.replace("python file","")
    elif "java file" in text:
        text = text.replace("java file","")
    elif "text file" in text:
        text = text.replace("text file","")
    elif "HTMl file" in text:
        text = text.replace("HTML file","")
    elif "CSS file" in text:
        text = text.replace("CSS file","")
    elif "JavaScript file" in text:
        text = text.replace("JavaScript file","")
    elif "JSON file" in text :
        text = text.replace("JSON file","")
    elif "XML file" in text:
        text = text.replace("XML file","")
    elif "CSV file" in text:
        text = text.replace("CSV file","")
    elif "markdown file" in text:
        text = text.replace("markdown file","")
    elif "yaml file" in text:
        text = text.replace("yaml file","")
    elif "image file" in text:
        text = text.replace("image file","")
    elif "video file" in text:
        text = text.replace("video file","")
    elif "audio file" in text:
        text = text.replace("audio file","")
    elif "PDF file" in text:
        text = text.replace("PDF file","")
    elif "word file" in text:
        text = text.replace("word file","")
    elif "excel file" in text:
        text = text.replace("excel file","")
    elif "powerpoint file" in text:
        text = text.replace("powerpoint file","")
    elif "zip file" in text:
        text = text.replace("zip file","")
    elif "tar file" in text:
        text = text.replace("tar file","")
    else:
        pass
    return text

def create_file(text):
    selected_ex = get_file_extension(text)
    text = update_text(text)
    if "named" in text or "with name" in text:
        text = text.replace("named","")
        text = text.replace("with name","")
        text = text.replacwe("create","")
        text = text.strip()
        with open(f"{text}{selected_ex}","w"):
            pass
    else:
        with open(f"demo{selected_ex}","w"):
            pass