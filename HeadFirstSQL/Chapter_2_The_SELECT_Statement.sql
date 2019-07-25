# Head First SQL

# Chapter 2
# The SELECT Stament: Gifted data retrieval


# Select语句可以窥探表
SELECT * # 与python相同, *表示所有内容
FROM my_contacts;

# 只呈现名字是Anne的语句
SELECT *
FROM my_contacts
WHERE first_name = 'Anne'; # 加上一个where语句, 注意不要用==


# Fruit table example
CREATE TABLE easy_drinks
(
    drink_name VARCHAR(20),
    main       VARCHAR(20),
    amount1    DECIMAL(4, 2),
    second     VARCHAR(20),
    amount2    DECIMAL(4, 2),
    directions VARCHAR(250)
);

# 另一种批量插入的形式
INSERT INTO easy_drinks
VALUES ('Blackthorn', 'tonic water', 1.5, 'pineapple juice', 1,
        'stir with ice, strain into cocktail glass with lemon twist'), # 这里接着用逗号分隔
       ('Blue Moon', 'soda', 1.5, 'blueberry juice', .75,
        'stir with ice, strain into cocktail glass with lemon twist'),
       ('Oh My Gosh', 'peach nectar', 1, 'pineapple juice', 1,
        'stir with ice, strain into shot glass'),
       ('Lime Fizz', 'Sprite', 1.5, 'lime juice', .75,
        'stir with ice, strain into cocktail glass'),
       ('Kiss on the Lips', 'cherrry juice', 2, 'apricot nectar', 7,
        'serve over ice with straw'),
       ('Hot Gold', 'peach nectar', 3, 'orange juice', 6,
        'pour hot orange juice in mug and add peach nectar'),
       ('Lone Tree', 'soda', 1.5, 'cherry juice', 0.75,
        'stir with ice, strain into cocktail glass'),
       ('Greyhound', 'soda', 1.5, 'grapefruit juice', 5, 'serve over ice, stir well'),
       ('Indian Summer', 'apple juice', 2, 'hot tea', 6, 'add juice to mug and top off with hot tea'),
       ('Bull Frog', 'iced tea', 1.5, 'lemonade', 5, 'serve over ice with lime slice'); # 最后才用分号




