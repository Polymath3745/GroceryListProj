from utils import cam
from utils import interpret

def main():
    """This will be used to take pic for now..."""
    """GUI will be made at a later date..."""

    try:
        choice  = input("Enter 'snap' to take picture of grocery list: ")
        if (choice == 'snap'):
            #cam.take_pic()
            print("Extracted text from picture :\n")
            interpret.extract()
        else:
            print("Invalid input. Please enter 'snap' to take a picture.")

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl + C) gracefully
        print("\nOperation canceled by user...")
    except Exception as e:
        print("An error occurred...", str(e))



if __name__ == '__main__':
    main()