#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>

int main()
{

    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Test");

    sf::CircleShape circle(100.f);
    circle.setFillColor(sf::Color::Green);
    circle.setPosition(200.f, 200.f);

    sf::Font font;
    if (!font.loadFromFile("D:/VS/2 semestr/ConsoleApplication8/ConsoleApplication8/tuffy.ttf"))
        return EXIT_FAILURE;
    sf::Text text("Hello :D", font, 50);
    text.setFillColor(sf::Color::Red);
    text.setPosition(240.f, 260.f);

    sf::SoundBuffer buffer;
    if (!buffer.loadFromFile("D:/VS/2 semestr/ConsoleApplication8/ConsoleApplication8/ding.flac"))
        return EXIT_FAILURE;
    sf::Sound sound(buffer);
    sound.play();

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(circle);
        window.draw(text);
        window.display();
    }

    return EXIT_SUCCESS;
}
