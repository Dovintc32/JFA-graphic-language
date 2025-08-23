#include <SFML/Graphics.hpp>
#include <iostream>
#include <fstream>
#include <json.hpp>
#include <cstdlib>
#include <func.h>

using json = nlohmann::json;
#include <string>



int main(int argc, char* argv[]) {
    json j = {{"File_name", argv[1]}};
    std::ofstream("Data/data_cpp.json") << j.dump(4);

    std::system("core\\python_.exe src\\parser.py");

    auto number_data = load_json("Data/Variables/number.json");
    auto string_data = load_json("Data/Variables/string.json");
    

    std::ifstream data_x("Data/data.json");
    json data;
    data_x >> data; 

    std::string name = data["Win"]["Name"];
    int SizeX = data["Win"]["SizeX"];
    int SizeY = data["Win"]["SizeY"];
    bool Open_Win = data["JFA SETTINGS"]["Status_Programm"]["Open_Win"];

    if (Open_Win == 1){

    sf::RenderWindow window(sf::VideoMode(SizeX, SizeY), name);
    
        while (window.isOpen()) {
            sf::Event event;
            while (window.pollEvent(event)) {
                if (event.type == sf::Event::Closed) {
                    window.close();
                }
            }
            window.clear(sf::Color::Black);
            window.display();    
        }
    }
    
    data["Win"] = {
        {"Name", ""},
        {"SizeX", 0},
        {"SizeY", 0}
    };
    data["JFA SETTINGS"]["Status_Programm"] = {
        {"Error_Line", ""},
        {"Stopped", false},
        {"Open_Win", false}
    };
    number_data["Numbers"] = json::object();
    string_data["String"] = json::object();
    
    save_json(number_data, "Data/Variables/number.json");
    save_json(string_data, "Data/Variables/string.json");
    std::ofstream("Data/data.json") << std::setw(4) << data;

    return 0;
}   