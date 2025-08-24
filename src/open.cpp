#include <SFML/Graphics.hpp>
#include <iostream>
#include <fstream>
#include <json.hpp>
#include <cstdlib>
#include "func.h"
using namespace std;

using json = nlohmann::json;
#include <string>



int main(int argc, char* argv[]) {
    json j = {{"File_name", argv[1]}};
    std::ofstream("Data/data_cpp.json") << j.dump(4);

    std::system("core\\python_.exe src\\parser.py");

    auto number_data = load_json("Data/Variables/number.json");
    auto string_data = load_json("Data/Variables/string.json");
    auto commads_data = load_json("Data/Variables/commands.json");
    auto data = load_json("Data/data.json");
    std::string name = data["Win"]["Name"];
    int SizeX = data["Win"]["SizeX"];
    int SizeY = data["Win"]["SizeY"];
    bool Open_Win = data["JFA SETTINGS"]["Status_Programm"]["Open_Win"];
    sf::Color backgroundColor(0, 0, 0);

    string cbr = "Colorize.background.rgb-1";
    string cbrx = cbr.substr(0, cbr.find('-'));

    if (Open_Win == 1){

    sf::RenderWindow window(sf::VideoMode(SizeX, SizeY), name);
    
        while (window.isOpen()) {
            sf::Event event;
            while (window.pollEvent(event)) {
                if (event.type == sf::Event::Closed) {
                    window.close();
                }
                
                for (const auto& [key, value] : commads_data.items()) {
                    size_t dash_pos = key.find('-');
                    if (dash_pos != std::string::npos) {
                        std::string prefix = key.substr(0, dash_pos);
                        if (prefix == "Colorize.background.rgb") {
                            backgroundColor = sf::Color(value[0], value[1], value[2]);
                            window.clear(backgroundColor);
                        }
                    }
                }
                // if (event.type == sf::Event::KeyReleased && event.key.code == sf::Keyboard::W) {
                //     std::cout << commads_data["Colorize.background.rgb"] << std::endl;
                // }
            }
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
    commads_data = json::object();

    save_json(commads_data, "Data/Variables/commands.json");
    save_json(number_data, "Data/Variables/number.json");
    save_json(string_data, "Data/Variables/string.json");
    std::ofstream("Data/data.json") << std::setw(4) << data;

    return 0;
}   