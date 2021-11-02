# Project Assignment: Marketing Attribution

## 1. Get familiar with the company.

- How many campaigns and sources does CoolTShirts use and how are they related?

  - The company has 8 campaigns and 6 sources. Each campaign is specific to only one source, as detailed in this table.

  - | utm_campaign                        | utm_source |
    | ----------------------------------- | ---------- |
    | getting-to-know-cool-tshirts        | nytimes    |
    | weekly-newsletter                   | email      |
    | ten-crazy-cool-tshirts-facts        | buzzfeed   |
    | retargetting-campaign               | email      |
    | retargetting-ad                     | facebook   |
    | interview-with-cool-tshirts-founder | medium     |
    | paid-search                         | google     |
    | cool-tshirts-search                 | google     |

- What pages are on their website?

  - The website is made up of 4 pages: Landing page, Shopping cart, Checkout and Purchase

    | page_name         |
    | ----------------- |
    | 1 - landing_page  |
    | 2 - shopping_cart |
    | 3 - checkout      |
    | 4 - purchase      |

## 2. What is the user journey?

- How many first touches is each campaign responsible for?

  - | utm_source | utm_campaign                        | COUNT(*) |
    | ---------- | ----------------------------------- | -------- |
    | medium     | interview-with-cool-tshirts-founder | 622      |
    | nytimes    | getting-to-know-cool-tshirts        | 612      |
    | buzzfeed   | ten-crazy-cool-tshirts-facts        | 576      |
    | google     | cool-tshirts-search                 | 169      |

- How many last touches is each campaign responsible for?

  - | utm_source | utm_campaign                        | COUNT(*) |
    | ---------- | ----------------------------------- | -------- |
    | email      | weekly-newsletter                   | 447      |
    | facebook   | retargetting-ad                     | 443      |
    | email      | retargetting-campaign               | 245      |
    | nytimes    | getting-to-know-cool-tshirts        | 232      |
    | buzzfeed   | ten-crazy-cool-tshirts-facts        | 190      |
    | medium     | interview-with-cool-tshirts-founder | 184      |
    | google     | paid-search                         | 178      |
    | google     | cool-tshirts-search                 | 60       |

- How many visitors make a purchase?

  - 361 users made a purchase 

- How many last touches *on the purchase page* is each campaign responsible for?

  - | utm_source | utm_campaign                        | COUNT(*) |
    | ---------- | ----------------------------------- | -------- |
    | email      | weekly-newsletter                   | 114      |
    | facebook   | retargetting-ad                     | 112      |
    | email      | retargetting-campaign               | 53       |
    | google     | paid-search                         | 52       |
    | buzzfeed   | ten-crazy-cool-tshirts-facts        | 9        |
    | nytimes    | getting-to-know-cool-tshirts        | 9        |
    | medium     | interview-with-cool-tshirts-founder | 7        |
    | google     | cool-tshirts-search                 | 2        |

- What is the typical user journey?

## 3. Optimize the campaign budget.

- CoolTShirts can re-invest in 5 campaigns. Which should they pick and why?

  - **Articles campaigns**: these campaigns were the main drivers of first touches and have been very successful in enticing people to find out more about the brand and the products and thus bring a lot of new leads to the top of the funnel.

    As a side benefit, these campaigns will also increase the brand authority, ranking and overall visibility in search engines, and it will lead to organically acquiring new customers in the long-term.

  - **Retargeting**: retargeting campaigns have been very successful in bringing back visitors, as well as in leading to a purchase. The most effective sources for this have been *emails* and *Facebook retargetting ads*.

  - **Newsletter**: the newsletter has proves to be a very effective way of re-engaging existing users and turning them into repeat customers.

- Recommended campaigns to re-invest in based on the results:

  - interview-with-cool-tshirts-founder
  - getting-to-know-cool-tshirts
  - ten-crazy-cool-tshirts-facts
  - weekly-newsletter on Email
  - retargetting-ad on Facebook
