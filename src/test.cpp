#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    sf::RenderWindow window(sf::VideoMode(600, 400), "SFML: Отпускание W");

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            // Проверяем, закрыто ли окно
            if (event.type == sf::Event::Closed) {
                window.close();
            }

            // Проверяем, была ли ОТПУЩЕНА клавиша W
            if (event.type == sf::Event::KeyReleased && event.key.code == sf::Keyboard::W) {
                std::cout << "Привет" << std::endl;
            }
        }

        window.clear(sf::Color::White);
        window.display();
    }

    return 0;
}