import pywhatkit as pw 

while True:
    print("=====>Welcome to text to handwritting converter🙏🙏🙏")
    text = input("=====>(type exit to quit)\nEnter the text that you want to convert it into hand written text \n😃😃")
    
    if text=='exit':
        print("===>>ThankYou boss come back later👍👍👍")
        break
    else:
        pw.text_to_handwriting(text,"res.png",[1,2,3])
        print("Successfully converted your text😎😎😎")