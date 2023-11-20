#include <fstream>
#include <iostream>
using namespace std;

// Different OSs use different CLI commands to run Python
#ifdef _WIN32
// TODO: If your Windows machine runs Python in CLI with "python" instead of "py", update this line.
const string python = "py";
#else
// TODO: If your Mac/Linux machine runs Python in CLI with "python3" instead of "python", update this line.
const string python = "python3";
#endif

/*
 * Prompts the user for a filename.
 * Allows the user to enter nothing to use the default pic (autumn.jpg).
 * If the file has extension jpg, jpeg, jpe, or png
 * and it exists in the project folder, return it.
 * Otherwise, return the default pic filename.
 */
string get_filename() {
    cout << "Enter filename: " << endl;
    string input;
    getline(cin, input);
    if (input.length() < 1) {
        input = "autumn.jpg";
    }
    int pos = input.rfind('.');
    if (pos == string::npos) {
        input = "autumn.jpg";
    }
    string ext = input.substr(pos+1);
    if (ext == "jpg" || ext == "jpeg" || ext == "gif") {
        return input;
    }
    return input;
}

/*
 * Prints the main menu of options:
 * (a) flip, (b) mirror, (c) invert, or (d) exit
 */
void print_menu(){
    cout << "Select an option: " << endl;
    cout << "Flip(a)" << endl;
    cout << "Mirror(b)" << endl;
    cout << "Invert(c)" << endl;
    cout << "Exit(d)" << endl;
}

/*
 * Prompts the user for one of the options from the menu.
 * Validates input: makes sure the user enters exactly one character
 * and that it is one of the four valid options.
 * If it is not valid, keep prompting for input until a valid option
 * is entered.
 */
char get_manip_choice() {
    cout << "Enter your choice as a single character a-d: " << endl;
    string input;
    getline(cin, input);
    while((input.length() > 1) || (input.length() < 1) || ((input != "a") && (input != "b") && (input != "c") && (input != "d"))) {
        if(input.length() > 1) {
            cout << "Invalid input. Enter a single character: " << endl;
            getline(cin, input);
        }
        else {
            cout << "No input. Enter your choice as a single character a-d: " << endl;
            getline(cin, input);
        }
    }
    char output = input[0];
    return output;
}

int main() {
    cout << "Welcome to the image manipulator!" << endl;
    string filename = get_filename();
    cout << "Using file " << filename << "." << endl;
    print_menu();
    char choice = get_manip_choice();
    cout << "Processing. Go to Python program when it opens. May take a few seconds." << endl;
    string command;


    switch (choice) {
        // Use command-line arguments to pass the filename and manipulate to the Python file
        case 'a':
            command = python + " render.py " + filename + " flip";
            break;
        case 'b':
            command = python + " render.py " + filename + " mirror";
            break;
        case 'c':
            command = python + " render.py " + filename + " invert";
            break;
    }
    system(command.c_str());
    return 0;
}
