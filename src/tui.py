import os

class Tui:
    @staticmethod   
    def print_lyrics(title: str, lyrics: str):
        for i in range(3):
            print()
            if i == 1:
                print(f"# {title} #", end='')
            else:
                for j in range(len(title)+4):
                    print("#", end='')
        print("\n\n")
        print(lyrics)
            
    @staticmethod
    def clear_term():
        os.system('cls' if os.name == 'nt' else 'clear')
