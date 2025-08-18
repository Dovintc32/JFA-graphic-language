#include <SFML/Graphics.hpp>
#include <iostream>
#include <fstream>
#include <json.hpp>
#include <cstdlib>

using json = nlohmann::json;

int main(int argc, char* argv[]) {

    json j = {{"File_name", argv[1]}};
    std::ofstream("Data/data_cpp.json") << j.dump(4);

    std::system("core\\python_.exe src\\parser.py");

    std::ifstream file("Data/data.json");
    json data;
    file >> data; 
    std::string name = data["Type"]["Win"]["Name"];
    int SizeX = data["Type"]["Win"]["SizeX"];
    int SizeY = data["Type"]["Win"]["SizeY"];
    bool Open_Win = data["Type"]["Win"]["Open_Win"];

    if (Open_Win == 1){

    sf::RenderWindow window(sf::VideoMode(SizeX, SizeY), name);
    std::cout << Open_Win;
    
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
    

    data["Type"]["Win"]["Name"] = "";
    std::ofstream("Data/data.json") << std::setw(4) << data;
    data["JFA SETTINGS"]["Status_Programm"]["Stopped"] = false;
    std::ofstream("Data/data.json") << std::setw(4) << data;

    return 0;
}   