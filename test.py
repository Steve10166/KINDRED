def breakmusic():
    print("S: So mean, you don't like my singing? I will stop playing music then!")
    ## add the coding
    return 0

def playmusic():
    print("S: You passed the vibe check, here is the song again!!")
    ## add the coding
    return 0

    

class MacroBreak(Macro):
    def run(self, ngrams: Ngrams, vars: Dict[str, Any], args: List[Any]):
        #^^DONT HAVE TO COPY THE TOP, JUST THESE IF ELSE STATEMENTS
        #ADD THIS TO EVERY GPT MACRO
        if ngrams.text() == "ssss":
            breakmusic()
            return False
        elif ngrams.text() == "pppp":
            playmusic()
            return False
        else:
            # INSERT WHERE THE NORMAL GPT FUNCTION IS SUPPOSE TO BE
            return True      


