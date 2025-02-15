#include <SFML/Graphics.hpp>

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "balls");

    sf::CircleShape ball1(20.f);
    ball1.setFillColor(sf::Color::Red);
    ball1.setPosition(400.f, 30.f);

    sf::CircleShape ball2(10.f);
    ball2.setFillColor(sf::Color::Green);
    ball2.setPosition(200.f, 30.f);

    sf::CircleShape ball3(30.f);
    ball3.setFillColor(sf::Color::Blue);
    ball3.setPosition(500.f, 30.f);

    float gravity = 0.0001f;
    float damping = 0.85f;

    float velocity1 = 0.04f;
    float velocity2 = 0.01f;
    float velocity3 = 0.2f;

    while (window.isOpen()) 
    {
        sf::Event event;
        while (window.pollEvent(event)) 
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        velocity1 += gravity;
        velocity2 += gravity;
        velocity3 += gravity;
        ball1.move(0.f, velocity1);
        ball2.move(0.f, velocity2);
        ball3.move(0.f, velocity3);

        if (ball1.getPosition().y + ball1.getRadius() >= 580.f)
        {
            ball1.setPosition(ball1.getPosition().x, 580.f - ball1.getRadius());
            velocity1 = -velocity1 * damping;
        }

        if (ball2.getPosition().y + ball2.getRadius() >= 590.f) 
        {
            ball2.setPosition(ball2.getPosition().x, 590.f - ball2.getRadius());
            velocity2 = -velocity2 * damping;
        }

        if (ball3.getPosition().y + ball3.getRadius() >= 570.f)
        {
            ball3.setPosition(ball3.getPosition().x, 570.f - ball3.getRadius());
            velocity3 = -velocity3 * damping;
        }
        window.clear();
        window.draw(ball1);
        window.draw(ball2);
        window.draw(ball3);
        window.display();
    }

    return 0;
}
