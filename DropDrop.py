"""Comment here"""
def main():
    """main"""
    cat = float(input())
    if cat >= 2:
        print("I'm so happy.")
    elif 1 <= cat < 2:
        result = float(4-cat)
        print("%.2f" %(result))
    else:
        print("I'm so sad.")
main()
